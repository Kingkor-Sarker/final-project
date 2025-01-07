from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt  
import os
from werkzeug.utils import secure_filename
from sqlalchemy.orm import relationship
# mydbconnection
local_server = True
app = Flask(__name__)
app.secret_key = 'sunvi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/learn'
db = SQLAlchemy(app)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

# DB Models (Tables)
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class user(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))  
    nid = db.Column(db.Integer, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    cooking = db.Column(db.Boolean, default=False)
    cleaning = db.Column(db.Boolean, default=False)
    washing_clothes = db.Column(db.Boolean, default=False)
    about_you = db.Column(db.String(255), nullable=True)
    img_path = db.Column(db.String(255), nullable=True)
    hourly_rate = db.Column(db.Float, nullable=False)  
    nid = db.Column(db.String(20), nullable=False)  
    is_booked = db.Column(db.Boolean, default=False)
    is_banned = db.Column(db.Boolean, default=False)
    is_verified = db.Column(db.Boolean, default=False)

from sqlalchemy.orm import relationship

class HireInfo(db.Model):
    __tablename__ = 'hireinfo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    total_payment = db.Column(db.Float, nullable=False)
    transaction_id = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    hire_status = db.Column(db.Boolean, default=False)

    # Relationship with user
    user = relationship('user', backref='hireinfo')

    # Relationship with worker
    worker = relationship('Worker', backref='hireinfo')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        # Update user profile logic here (e.g., update username, email, password)
        current_user.username = request.form['username']  # UPDATE users SET username = 'new_username' WHERE id = current_user.id;
        current_user.email = request.form['email']        # UPDATE users SET email = 'new_email' WHERE id = current_user.id;
        db.session.commit()                               # COMMIT;
        return redirect(url_for('profile'))  # Redirect back to the profile page after saving changes
    return render_template('profile.html')

@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('index.html')
    return render_template('index.html')

@app.route('/adminban')
@login_required
def adminban():
    if not current_user.is_admin:
        flash("You are not authorized to access this page.", "danger")
        return redirect(url_for('index'))
    

    workers_list = Worker.query.all()  # SELECT * FROM workers;
    
    return render_template('adminban.html', workers=workers_list)

@app.route('/ban_worker/<int:worker_id>', methods=['POST'])
@login_required
def ban_worker(worker_id):
    if not current_user.is_admin:
        flash("You are not authorized to perform this action.", "danger")
        return redirect(url_for('index'))
    
    worker = Worker.query.get_or_404(worker_id)  # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    worker.is_banned = True  
    db.session.commit()       
    flash(f"Worker {worker.name} has been banned.", "success")
    return redirect(url_for('adminban'))

@app.route('/unban_worker/<int:worker_id>', methods=['POST'])
@login_required
def unban_worker(worker_id):
    if not current_user.is_admin:
        flash("You are not authorized to perform this action.", "danger")
        return redirect(url_for('index'))
    
    worker = Worker.query.get_or_404(worker_id)    # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    worker.is_banned = False                      
    db.session.commit()                             
    flash(f"Worker {worker.name} has been unbanned.", "success")
    return redirect(url_for('adminban'))

@app.route('/adminbook', methods=['GET',"POST"])
@login_required
def adminbook():
    workers = Worker.query.all()  # SELECT * FROM workers;
    return render_template('adminbook.html', workers=workers)

@app.route('/unbook_worker/<int:worker_id>', methods=['POST'])
@login_required
def unbook_worker(worker_id):
    if not current_user.is_admin:
        flash("You are not authorized to perform this action.", "danger")
        return redirect(url_for('index'))
    
    worker = Worker.query.get_or_404(worker_id)  # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    worker.is_booked = False                     
    db.session.commit()                          
    flash(f"Worker {worker.name} has been unbooked.", "success")
    return redirect(url_for('adminbook'))


@app.route('/adminpayment', methods=['GET',"POST"])
@login_required
def adminpayment():
    hireinfo = HireInfo.query.filter_by(hire_status=False).all()  
    # SELECT * FROM hire_info WHERE hire_status = FALSE;
    
    for info in hireinfo:
        info.user = info.user  # This typically involves a JOIN, e.g., SELECT * FROM hire_info JOIN users ON hire_info.user_id = users.id WHERE hire_info.hire_status = FALSE;
        info.worker = info.worker 
    return render_template('adminpayment.html', hireinfo=hireinfo)

@app.route('/payment/done/<int:hire_id>', methods=['POST'])
@login_required
def payment_done(hire_id):
    hire_info = HireInfo.query.get(hire_id)  # SELECT * FROM hire_info WHERE id = hire_id LIMIT 1;
    if hire_info:
        hire_info.hire_status = True  # UPDATE hire_info SET hire_status = TRUE WHERE id = hire_id;
    worker = Worker.query.get(hire_info.worker_id)  # SELECT * FROM workers WHERE id = hire_info.worker_id LIMIT 1;
    if worker:
        worker.is_booked = True    # UPDATE workers SET is_booked = TRUE WHERE id = worker_id;
    db.session.commit()            
    flash("Payment marked as Done.", "success")
    return redirect(url_for('adminpayment'))

@app.route('/payment/reject/<int:hire_id>', methods=['POST'])
@login_required
def reject_payment(hire_id):
    # Fetch the hire record
    hire_info = HireInfo.query.get(hire_id)  # SELECT * FROM hire_info WHERE id = hire_id LIMIT 1;
    if hire_info:
        hire_info.hire_status = True  # UPDATE hire_info SET hire_status = TRUE WHERE id = hire_id;
        
        worker = Worker.query.get(hire_info.worker_id)  # SELECT * FROM workers WHERE id = hire_info.worker_id LIMIT 1;
        if worker:
            worker.is_booked = False  # UPDATE workers SET is_booked = FALSE WHERE id = worker_id;
    
        db.session.commit()        
        flash("Transaction rejected successfully and worker status updated.", "warning")
    return redirect(url_for('adminpayment'))


@app.route('/process_hire/<int:worker_id>', methods=['POST'])
def process_hire(worker_id):
    worker = Worker.query.get_or_404(worker_id)  # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    # Additional logic for payment or confirmation
    flash(f"Worker {worker.name} hire process initiated.", "success")
    return redirect(url_for('workers'))

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/workers')
def workers():
    workers_list = Worker.query.filter_by(is_banned=False, is_booked=False, is_verified=True).all()  
    # SELECT * FROM workers WHERE is_banned = FALSE AND is_booked = FALSE AND is_verified = TRUE;
    for worker in workers_list:
        worker.img_path = worker.img_path.replace(os.sep, '/')
    return render_template('workers.html', workers=workers_list)

app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':       
        # Ensure the upload folder exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        about_you = request.form.get('about_you')
        hourly_rate = request.form.get('hourly_rate')
        nid = request.form.get('nid')

        cooking = 'cooking' in request.form  
        cleaning = 'cleaning' in request.form
        washing_clothes = 'washing_clothes' in request.form

        # Handle image upload
        file = request.files['image']
        if file and allowed_file(file.filename):  # Assuming allowed_file function is in place
            filename = secure_filename(file.filename) 
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Full path stored in the database
            file.save(img_path)  
        else:
            img_path = None  

        new_worker = Worker(
            name=name, 
            email=email, 
            phone=phone, 
            cooking=cooking,  
            cleaning=cleaning,  
            washing_clothes=washing_clothes,  
            about_you=about_you, 
            img_path=img_path,  
            hourly_rate=hourly_rate,  
            nid=nid,  
            is_banned=False,
            is_booked=False,
            is_verified=False
        )
        db.session.add(new_worker)  # INSERT operation as above
        db.session.commit()          # COMMIT;

        flash("Worker application successfully submitted!", "success")
        return render_template('success.html')  

    return render_template('apply.html')


@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("You are not authorized to access this page.", "danger")
        return redirect(url_for('index'))
    
    # Fetch workers with is_verified set to False
    pending_workers = Worker.query.filter_by(is_verified=False).all()  
    # SELECT * FROM workers WHERE is_verified = FALSE;
    
    return render_template('admin_dashboard.html', pending_workers=pending_workers)



@app.route('/approve_worker/<int:worker_id>', methods=['POST'])
@login_required
def approve_worker(worker_id):
    if not current_user.is_admin:
        flash("You are not authorized to perform this action.", "danger")
        return redirect(url_for('index'))
    
    worker = Worker.query.get_or_404(worker_id)  # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    worker.is_verified = True                     # UPDATE workers SET is_verified = TRUE WHERE id = worker_id;
    db.session.commit()                           # COMMIT;
    flash(f"Worker {worker.name} has been approved.", "success")
    return redirect(url_for('admin_dashboard'))

@app.route('/reject_worker/<int:worker_id>', methods=['POST'])
@login_required
def reject_worker(worker_id):
    if not current_user.is_admin:
        flash("You are not authorized to perform this action.", "danger")
        return redirect(url_for('index'))
    
    worker = Worker.query.get_or_404(worker_id)   # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    worker.is_verified = False                     # UPDATE workers SET is_verified = FALSE WHERE id = worker_id;
    # db.session.delete(worker)                   # DELETE FROM workers WHERE id = worker_id;
    db.session.commit()                            # COMMIT;
    flash(f"Worker {worker.name} has been rejected and removed from the database.", "success")
    return redirect(url_for('admin_dashboard'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    hire_details = session.get('hire_details')
    if not hire_details:
        flash("No hiring details found. Please start again.", "danger")
        return redirect(url_for('workers'))

    if request.method == 'POST':
        transaction_id = request.form.get('transaction_id')

        if not transaction_id:
            flash("Transaction ID is required.", "danger")
            return redirect(url_for('payment'))

        # Save the hire info to the database
        hire_info = HireInfo(
            user_id=current_user.id,
            worker_id=hire_details['worker_id'],
            hours=hire_details['hours'],
            days=hire_details['days'],
            total_payment=hire_details['total_payment'],
            transaction_id=transaction_id
        )
        # INSERT INTO hire_info (user_id, worker_id, hours, days, total_payment, transaction_id) VALUES (...);
        db.session.add(hire_info)  # INSERT operation as above

        # Update worker's is_booked to 1 (active)
        worker = Worker.query.get(hire_details['worker_id'])  # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
        if worker:
            print(f"Worker found: {worker.id}, Current book status: {worker.is_booked}")
            worker.is_booked = True  # UPDATE workers SET is_booked = TRUE WHERE id = worker_id;
            db.session.commit()      # COMMIT;

        # Commit the session and clear session
        db.session.commit()          # COMMIT;

        session.pop('hire_details', None)
        flash("Payment successful. Worker hired!", "success")
        return redirect(url_for('workers'))

    return render_template('payment.html', hire_details=hire_details)

@app.route('/hire/<int:worker_id>', methods=['GET', 'POST'])
@login_required
def hire_worker(worker_id):
    worker = Worker.query.get_or_404(worker_id)  # SELECT * FROM workers WHERE id = worker_id LIMIT 1;
    
    if request.method == 'POST':
        # Get hours and days from the form
        hours = int(request.form.get('hours'))
        days = int(request.form.get('days'))
        total_payment = hours * days * worker.hourly_rate
        
        # Save details in session temporarily
        session['hire_details'] = {
            'worker_id': worker_id,
            'hours': hours,
            'days': days,
            'total_payment': total_payment
        }
        return redirect(url_for('payment'))  # Redirect to the payment page

    return render_template('hire_confirmation.html', worker=worker)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nid = request.form.get('nid')
        username = request.form.get('username')

        # Check for existing email or NID
        if user.query.filter_by(email=email).first():  # SELECT * FROM users WHERE email = 'email' LIMIT 1;
            return render_template('signup.html', error="Email already exists.")
        if user.query.filter_by(nid=nid).first():      # SELECT * FROM users WHERE nid = 'nid' LIMIT 1;
            return render_template('signup.html', error="NID already exists.")

        # Encrypt password 
        encpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = user(username=username, email=email, password=encpassword, nid=nid)
        # INSERT INTO users (username, email, password, nid) VALUES (...);
        db.session.add(new_user)  # INSERT operation as above
        try:
            db.session.commit()      # COMMIT;
        except Exception as e:
            db.session.rollback()    # ROLLBACK;
            return render_template('signup.html', error="An error occurred while saving to the database.")

        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_instance = user.query.filter_by(email=email).first()  # SELECT * FROM users WHERE email = 'email' LIMIT 1;

        if user_instance and bcrypt.checkpw(password.encode('utf-8'), user_instance.password.encode('utf-8')):
            login_user(user_instance)  
            
            if current_user.is_admin: 
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('index'))  
        else:
            return render_template('login.html', error="Invalid email or password.")
    
    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)



