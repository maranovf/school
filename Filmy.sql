-- Adminer 4.8.1 MySQL 5.1.72-community dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `Filmy`;
CREATE DATABASE `filmy` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `Filmy`;

DROP TABLE IF EXISTS `filmy`;
CREATE TABLE `filmy` (
  `nazev` varchar(64) NOT NULL,
  `rok_vydani` int(11) NOT NULL,
  `delka` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `filmy` (`nazev`, `rok_vydani`, `delka`) VALUES
('Periskop nahoru a dolu',	1990,	105),
('Batman',	2008,	206);

DROP TABLE IF EXISTS `herci`;
CREATE TABLE `herci` (
  `Jmeno_a_prijimeni` varchar(128) NOT NULL,
  `pocet_filmu` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `herci` (`Jmeno_a_prijimeni`, `pocet_filmu`) VALUES
('Karel Gott',	7),
('Kelsey Grammer',	16);

DROP TABLE IF EXISTS `zanry`;
CREATE TABLE `zanry` (
  `nazev` varchar(128) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `zanry` (`nazev`) VALUES
('Sci-fi'),
('Komedie'),
('Ak?ní');

-- 2022-12-14 07:22:48
