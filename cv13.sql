-- Adminer 4.8.1 MySQL 5.1.72-community dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `cv13`;
CREATE DATABASE `cv13` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cv13`;

DROP TABLE IF EXISTS `cv`;
CREATE TABLE `cv` (
  `idkniha` int(11) NOT NULL,
  `kniha_nazev` varchar(40) NOT NULL,
  `kniha_pocet_stran` int(11) NOT NULL,
  `kniha_autor` varchar(64) NOT NULL,
  `kniha_popis` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `cv` (`idkniha`, `kniha_nazev`, `kniha_pocet_stran`, `kniha_autor`, `kniha_popis`) VALUES
(1,	'Zaznam 1',	256,	'Autor 1',	''),
(2,	'Kniha 2',	512,	'Autor 2',	'');

-- 2022-12-07 09:19:46
