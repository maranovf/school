-- Adminer 4.8.1 MySQL 5.1.72-community dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `auta`;
CREATE TABLE `auta` (
  `id` int(11) NOT NULL,
  `nazev` varchar(64) NOT NULL,
  `znacka` varchar(64) NOT NULL,
  `barva` varchar(64) NOT NULL,
  `rok_vyroby` int(11) NOT NULL,
  `objem_motoru` int(11) NOT NULL,
  `vykon` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `auta` (`id`, `nazev`, `znacka`, `barva`, `rok_vyroby`, `objem_motoru`, `vykon`) VALUES
(1,	'Fabia',	'Škoda',	'bílá',	2010,	1,	75),
(2,	'Fabia',	'Škoda',	'St?íbrná',	2002,	1,	105),
(3,	'Vectra',	'Opel',	'Modrá',	1990,	2,	90),
(4,	'Astra',	'Opel',	'Bílá',	2000,	2,	105);

-- 2022-12-12 07:22:11
