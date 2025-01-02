-- Adminer 4.8.1 MySQL 5.1.72-community dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `cv17`;
CREATE DATABASE `cv17` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cv17`;

DROP TABLE IF EXISTS `kategorie`;
CREATE TABLE `kategorie` (
  `id` int(11) NOT NULL,
  `nazev_kategorie` varchar(64) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `kategorie_id` int(11) NOT NULL,
  KEY `id` (`kategorie_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


-- 2023-01-18 07:37:48
