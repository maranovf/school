-- Adminer 4.8.1 MySQL 5.1.72-community dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `test`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `iduser` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `last_login` datetime NOT NULL,
  `role` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `users` (`iduser`, `username`, `password`, `email`, `last_login`, `role`) VALUES
(1,	'maranovo',	'uhuih',	'hbzuz',	'0000-00-00 00:00:00',	1),
(2,	'ijjiuh',	'bgguzgb',	'guzgft',	'0000-00-00 00:00:00',	2);

-- 2022-12-07 09:01:40
