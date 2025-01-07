-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2025 at 11:10 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `learn`
--

-- --------------------------------------------------------

--
-- Table structure for table `hireinfo`
--

CREATE TABLE `hireinfo` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `worker_id` int(11) NOT NULL,
  `hours` int(11) NOT NULL,
  `days` int(11) NOT NULL,
  `total_payment` float NOT NULL,
  `transaction_id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `hire_status` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hireinfo`
--

INSERT INTO `hireinfo` (`id`, `user_id`, `worker_id`, `hours`, `days`, `total_payment`, `transaction_id`, `created_at`, `hire_status`) VALUES
(5, 17, 30, 2, 7, 322, 'adafaf', '2025-01-06 23:58:58', 1),
(6, 12, 31, 1, 4, 136, 'ere', '2025-01-07 00:39:47', 1),
(7, 19, 34, 23, 2, 1012, '123456', '2025-01-07 16:42:28', 1),
(8, 19, 32, 3, 3, 198, '1234', '2025-01-07 17:04:30', 1),
(9, 19, 23, 2, 1, 200, '456yu', '2025-01-07 17:11:59', 1),
(10, 19, 23, 6, 3, 1800, 'testtnx', '2025-01-07 20:17:11', 1),
(11, 19, 23, 1, 6, 600, 'tnx-hash', '2025-01-07 20:21:36', 1),
(12, 19, 29, 4, 5, 460, '4567y', '2025-01-07 20:25:46', 1),
(13, 19, 30, 12, 1, 276, 'ertgjgb', '2025-01-07 20:44:17', 1),
(14, 19, 30, 3, 30, 2070, 'rtyuik,d', '2025-01-07 20:50:00', 1),
(15, 19, 31, 5, 5, 850, 'tnxxxx', '2025-01-07 21:02:41', 1),
(16, 19, 23, 21, 2, 4200, 'tnxxx', '2025-01-07 21:32:15', 1),
(17, 19, 23, 12, 2, 2400, 'test', '2025-01-07 21:35:27', 1),
(18, 19, 23, 2, 5, 1000, 'test tedfnkasdn', '2025-01-07 21:39:50', 1),
(19, 19, 23, 34, 44, 149600, 'afasknk', '2025-01-07 22:12:34', 1),
(20, 19, 23, 1, 3, 300, 'dasdasf', '2025-01-07 22:13:06', 1),
(21, 19, 23, 3, 2, 600, 'fgsf', '2025-01-07 22:34:13', 1),
(22, 19, 23, 12, 2, 2400, '3456', '2025-01-07 22:36:19', 1),
(23, 19, 29, 3, 2, 138, '23erf', '2025-01-07 22:45:10', 1),
(24, 19, 23, 1, 1, 100, '1wedf', '2025-01-07 22:50:55', 1),
(25, 19, 23, 23234, 3, 6970200, 'hjwud', '2025-01-07 23:40:20', 1),
(26, 19, 30, 12, 1, 276, 'erfghj', '2025-01-08 01:40:35', 1),
(27, 19, 43, 3, 2, 1200, '2345rdrytf', '2025-01-08 03:58:20', 1);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`, `email`) VALUES
(1, 'sunvi', 'afiffa@kkks'),
(2, 'riff', 'rfaaaaffkks');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nid` int(11) NOT NULL,
  `password` varchar(100) NOT NULL,
  `is_admin` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `nid`, `password`, `is_admin`) VALUES
(11, 'Kingkor Sarker Showmick ', 'kingkor.online@gmail.com', 1223456789, '$2b$12$i.gBonqWOMVb30JGpasjbuToSDcGBGb6n1J3nIzg/GyOQ8mhBFUcS', 1),
(12, 'sunvimama', 'afifsunvi@gmail.com', 3333345, '$2b$12$nT9DX26fu4nsCwDUg9sXOeMEBc86bhEXcSYeRUTFpyOd7e/pvZvZ2', 1),
(13, 'mou', 'nazmulrifat2002@gmail.com', 1234525245, '$2b$12$IOpKs30bVDPIucCLpqtfz.YfAbe1.tnFnfSsYFlK68BJ7mStmTX.O', 0),
(14, 'sunvi', 'awdwddw@gmail.com', 2147483647, '$2b$12$ezKFiydy3Th6QE8ezKR8Begc1qHoBxJ8s57ghVkCk9mygO64PSrUu', 0),
(16, 'awdAWD', 'kingor@gmail.com', 1212312312, '$2b$12$Rmac/inPEsHUMtMfOXHhV.yfd0PNLQ1Wnjo0ZYClb5hp2LmQivay.', 0),
(17, 'kigkjig', 'qwerty@gmail.com', 2324567, '$2b$12$8yIxGOE7gauTTY7Uo9m52unb6i7Qnzf289Tm0vNMksRJvrJ8.8Mym', 0),
(19, 'showmickk', 'showmick@gmail.com', 345678, '$2b$12$MK98rjPKQQrhW4pRK4bwaOerMbLA9mN1Yvxwrd1ps1SSlJ1z5mn/m', 0);

-- --------------------------------------------------------

--
-- Table structure for table `worker`
--

CREATE TABLE `worker` (
  `Name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `cooking` tinyint(1) NOT NULL,
  `cleaning` tinyint(1) NOT NULL,
  `washing_clothes` tinyint(1) NOT NULL DEFAULT 0,
  `about_you` varchar(255) DEFAULT NULL,
  `img_path` varchar(255) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `hourly_rate` int(11) NOT NULL,
  `nid` int(11) NOT NULL,
  `is_banned` tinyint(1) DEFAULT 0,
  `is_booked` tinyint(1) DEFAULT 0,
  `is_verified` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `worker`
--

INSERT INTO `worker` (`Name`, `email`, `phone`, `cooking`, `cleaning`, `washing_clothes`, `about_you`, `img_path`, `id`, `hourly_rate`, `nid`, `is_banned`, `is_booked`, `is_verified`) VALUES
('kingkhor', 'qwer@gmail.com', 1762591405, 1, 1, 1, 'shera bhai', 'static/uploads\\peakpx.jpg', 23, 100, 32423, 0, 0, 1),
('abdullah', 'qeqeeq@gmail.com', 123131414, 1, 1, 1, 'wwwwww', 'static/uploads\\462566399_1537299004377084_7274668106052628298_n.jpg', 29, 23, 112312311, 1, 0, 1),
('jhandubalm', 'awdawd@gmail.com', 9875435, 1, 1, 1, 'admin', 'static/uploads\\460328177_8417055538410036_5881454934776056719_n.jpg', 30, 23, 162452, 0, 0, 1),
('mou', 'nazmulrifat2002@gmail.com', 454545345, 1, 1, 1, 'yyyyyyyyyyyy', 'static/uploads\\460387012_8417055298410060_5351592648454538396_n.jpg', 31, 34, 4424424, 0, 0, 1),
('Palworld', 'kingor@gmail.com', 2147483647, 1, 1, 1, 'qweqweqwe3', 'static/uploads\\460627438_8417055311743392_9047183548716854944_n.jpg', 32, 22, 2223211, 0, 0, 1),
('palworld2', 'dede@gmail.com', 24425255, 1, 1, 1, 'wqeq', 'static/uploads\\304942536_538922978234561_6407103211231101181_n.jpg', 34, 22, 155612, 0, 0, 1),
('qweqwer', 'trerrwq@gmail.com', 12124566, 1, 1, 1, 'eee', 'static/uploads\\desktop-wallpaper-floating-in-space-by-visualdon-live-2d-space.jpg', 35, 54, 222451, 0, 0, 1),
('king', 'king@gmail.com', 234567, 1, 1, 1, 'dtrdrdddiy', 'static/uploads\\Screenshot_2023-09-18_221702.png', 36, 100, 2147483647, 1, 0, 1),
('kingkorrr', 'ijfiwjf@gmail.com', 234567, 1, 1, 1, 'iodjoijdwe', 'd:\\final-project\\flask\\static/uploads\\395478134_1699366107226606_3605307529683354272_n.jpg', 39, 200, 5775544, 0, 0, 1),
('jdwoiejdoijed', 'kidei@gmail.com', 56787654, 1, 1, 1, 'ajoja', 'd:\\final-project\\flask\\static/uploads\\wallpapersden.com_76671-3840x2160.jpg', 40, 499, 109835491, 0, 0, 1),
('joker', 'joker@gmail.com', 2147483647, 1, 1, 1, 'why so serious >', 'd:\\final-project\\flask\\static/uploads\\wp2662098-joker-wallpaper-widescreen.jpg', 41, 1999, 9371023, 0, 0, 1),
('Ridika bua', 'ridika@gmail.com', 345678765, 0, 1, 1, 'hi i am a bua', 'd:\\final-project\\flask\\static/uploads\\wallpaperflare.com_wallpaper_8.jpg', 43, 200, 80392311, 0, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hireinfo`
--
ALTER TABLE `hireinfo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `worker_id` (`worker_id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `nid` (`nid`);

--
-- Indexes for table `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nid` (`nid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hireinfo`
--
ALTER TABLE `hireinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `worker`
--
ALTER TABLE `worker`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hireinfo`
--
ALTER TABLE `hireinfo`
  ADD CONSTRAINT `hireinfo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `hireinfo_ibfk_2` FOREIGN KEY (`worker_id`) REFERENCES `worker` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
