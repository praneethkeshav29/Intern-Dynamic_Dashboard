-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2019 at 01:06 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flat`
--

-- --------------------------------------------------------

--
-- Table structure for table `clinionsources`
--

CREATE TABLE `clinionsources` (
  `id` int(11) NOT NULL,
  `webapi` varchar(255) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clinionsources`
--

INSERT INTO `clinionsources` (`id`, `webapi`, `webapiurl`, `webuser`, `webpass`, `mysql`, `mysqlurl`, `mysqldb`, `mysqluser`, `mysqlpass`, `sqlserver`, `sqlserverurl`, `sqlserverdb`, `sqlserveruser`, `sqlserverpass`) VALUES
(1, 'webapi', 'b\'aHR0cDovL2N0bXNhcGkucXVhZDF0ZXN0LmNvbTo4Njg3L2FwaS9hZG1pbi9zdHVkeXN0YXR1c2NvdW50P0NvbXBhbnlJZD1URVNUIFB6TUoxRHY2\'', 'b\'YWRtaW4=\'', 'b\'YWRtaW4=\'', 'mysql', 'b\'YmVuYyg=\'', 'b\'WkFQJW4lcyVuJXMlbiVzJW4lcyVuJXMlbiVzJW4lcyVuJXMlbiVzJW4lcyVuJXMlbiVzJW4lcyVuJXMlbiVzJW4lcyVuJXMlbiVzJW4lcyVuJXM=\'', 'b\'YWFh\'', 'b\'YWFhYWFh\'', 'sqlserver', 'hello', 'hello', 'admin', 'admin'),
(40, 'webapi', '', 'aaa', 'aaaaaa', 'mysql', 'b\'MjAuMC4wLjUy\'', 'hello', 'admin', 'password', 'sqlserver', 'aa', 'aa', 'aaa@aaa.com', 'aaaaaa'),
(41, 'webapi', '', '', '', 'mysql', 'b\'MjAuMC4wLjUy\'', 'hello', 'admin', 'password', NULL, NULL, NULL, NULL, NULL),
(43, 'webapi', 'aaa', 'w@w.w', 'wwwwww', 'mysql', 'b\'MjAuMC4wLjUy\'', 'hello', 'admin', 'password', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ctmssources`
--

CREATE TABLE `ctmssources` (
  `id` int(11) NOT NULL,
  `webapi` varchar(2555) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ctmssources`
--

INSERT INTO `ctmssources` (`id`, `webapi`, `webapiurl`, `webuser`, `webpass`, `mysql`, `mysqlurl`, `mysqldb`, `mysqluser`, `mysqlpass`, `sqlserver`, `sqlserverurl`, `sqlserverdb`, `sqlserveruser`, `sqlserverpass`) VALUES
(1, 'webapi', 'b\'aHR0cDovL2N0bXNhcGkucXVhZDF0ZXN0LmNvbTo4Njg3L2FwaS9hZG1pbi9zdHVkeXN0YXR1c2NvdW50P0NvbXBhbnlJZD1URVNUIFB6TUoxRHY2\'', 'b\'YWRtaW4=\'', 'b\'YWRtaW4=\'', 'mysql', 'b\'YWJj\'', 'b\'YWJj\'', 'b\'YWRtaW4=\'', 'b\'YWRtaW4=\'', 'sqlserver', 'yo', 'yo', 'admin', 'admin'),
(40, 'webapi', 'http://ctmsapi.quad1test.com:8687/api/admin/studystatuscount?CompanyId=TEST%20PzMJ1Dv6', 'aaa', 'aaaaaa', 'mysql', 'b\'YWFhd3I=\'', 'b\'YWE=\'', 'b\'YWFh\'', 'b\'YWFhYWFh\'', 'sqlserver', 'aa', 'aa', 'aaa@aaa.com', 'aaaaaa'),
(41, 'webapi', 'ctmsab', 'pk@pk.com', 'aaaaaa', 'mysql', 'ctab', 'ctab', 'pk@pk.com', 'aaaaaa', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dash`
--

CREATE TABLE `dash` (
  `id` int(11) NOT NULL,
  `webapi` varchar(255) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dashsources`
--

CREATE TABLE `dashsources` (
  `id` int(11) NOT NULL,
  `webapi` varchar(255) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dopsources`
--

CREATE TABLE `dopsources` (
  `id` int(11) NOT NULL,
  `webapi` varchar(255) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `npasources`
--

CREATE TABLE `npasources` (
  `id` int(11) NOT NULL,
  `webapi` varchar(255) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `npasources`
--

INSERT INTO `npasources` (`id`, `webapi`, `webapiurl`, `webuser`, `webpass`, `mysql`, `mysqlurl`, `mysqldb`, `mysqluser`, `mysqlpass`, `sqlserver`, `sqlserverurl`, `sqlserverdb`, `sqlserveruser`, `sqlserverpass`) VALUES
(1, 'webapi', 'b\'aHR0cDovL2N0bXNhcGkucXVhZDF0ZXN0LmNvbTo4Njg3L2FwaS9hZG1pbi9zdHVkeXN0YXR1c2NvdW50P0NvbXBhbnlJZD1URVNUIFB6TUoxRHY2\'', 'admin', 'admin', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `npsources`
--

CREATE TABLE `npsources` (
  `id` int(11) NOT NULL,
  `webapi` varchar(255) NOT NULL,
  `webapiurl` varchar(255) DEFAULT NULL,
  `webuser` varchar(255) DEFAULT NULL,
  `webpass` varchar(255) DEFAULT NULL,
  `mysql` varchar(255) DEFAULT NULL,
  `mysqlurl` varchar(255) DEFAULT NULL,
  `mysqldb` varchar(255) DEFAULT NULL,
  `mysqluser` varchar(255) DEFAULT NULL,
  `mysqlpass` varchar(255) DEFAULT NULL,
  `sqlserver` varchar(255) DEFAULT NULL,
  `sqlserverurl` varchar(255) DEFAULT NULL,
  `sqlserverdb` varchar(255) DEFAULT NULL,
  `sqlserveruser` varchar(255) DEFAULT NULL,
  `sqlserverpass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `npsources`
--

INSERT INTO `npsources` (`id`, `webapi`, `webapiurl`, `webuser`, `webpass`, `mysql`, `mysqlurl`, `mysqldb`, `mysqluser`, `mysqlpass`, `sqlserver`, `sqlserverurl`, `sqlserverdb`, `sqlserveruser`, `sqlserverpass`) VALUES
(1, 'webapi', 'b\'ZXFl\'', 'admin', '21232f297a57a5a743894a0e4a801fc3', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `name`, `description`) VALUES
(2, 'superuser', NULL),
(3, 'clinion', NULL),
(4, 'ctms', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `roles_users`
--

CREATE TABLE `roles_users` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `roles_users`
--

INSERT INTO `roles_users` (`user_id`, `role_id`) VALUES
(1, 2),
(1, 3),
(1, 4),
(44, 3),
(44, 2),
(153, 4),
(154, 3),
(155, 3);

-- --------------------------------------------------------

--
-- Table structure for table `todos`
--

CREATE TABLE `todos` (
  `todo_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `text` varchar(255) NOT NULL,
  `done` int(255) NOT NULL,
  `user_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `todos`
--

INSERT INTO `todos` (`todo_id`, `title`, `text`, `done`, `user_id`) VALUES
(1, 'clinion', 'clinion', 0, 27),
(2, 'clinion', 'clinion1', 0, 28);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `active` int(1) DEFAULT NULL,
  `confirmed_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `email`, `password`, `active`, `confirmed_at`) VALUES
(1, 'Admin', NULL, 'admin', '$pbkdf2-sha512$25000$ao0xhpDSWss5h7AW4rzXug$i1jPSNHLiUQLok1Vb1Jq18PoRdF9QwK3UXZ4KOVXCgbmw19g73W3pmticT3Pozza4wmGmvzTO6OIP9TrNjJVKg', 1, NULL),
(44, 'Nikshith', 'Reddy', 'nikshith@q.com', 'qwerty@123', 1, '2019-05-17 14:54:00'),
(153, 'praneeth', NULL, 'praneeth', 'qwerty@123', 1, '2019-05-06 16:12:00'),
(154, 'ae', 'eg', 'ee', 'ee', 1, '2019-05-01 17:08:00'),
(155, 'ssd', 'sda', 'ds@a.com', 'dq', 1, '2019-05-07 15:08:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clinionsources`
--
ALTER TABLE `clinionsources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ctmssources`
--
ALTER TABLE `ctmssources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dash`
--
ALTER TABLE `dash`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dashsources`
--
ALTER TABLE `dashsources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dopsources`
--
ALTER TABLE `dopsources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `npasources`
--
ALTER TABLE `npasources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `npsources`
--
ALTER TABLE `npsources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `roles_users`
--
ALTER TABLE `roles_users`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `todos`
--
ALTER TABLE `todos`
  ADD PRIMARY KEY (`todo_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `todos`
--
ALTER TABLE `todos`
  MODIFY `todo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=156;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `roles_users`
--
ALTER TABLE `roles_users`
  ADD CONSTRAINT `roles_users_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `roles_users_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
