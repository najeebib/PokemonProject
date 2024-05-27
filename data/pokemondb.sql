-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3308
-- Generation Time: May 27, 2024 at 09:09 AM
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
-- Database: `pokemondb`
--

-- --------------------------------------------------------

--
-- Table structure for table `pokedex`
--

CREATE TABLE `pokedex` (
  `pokedex_id` int(11) NOT NULL,
  `pokemon_id` int(11) DEFAULT NULL,
  `trainer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pokemons`
--

CREATE TABLE `pokemons` (
  `pokemon_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pokemontypes`
--

CREATE TABLE `pokemontypes` (
  `pokemon_types_id` int(11) NOT NULL,
  `pokemon_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trainers`
--

CREATE TABLE `trainers` (
  `trainer_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `town` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

CREATE TABLE `types` (
  `types_id` int(11) NOT NULL,
  `pokemon_type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pokedex`
--
ALTER TABLE `pokedex`
  ADD PRIMARY KEY (`pokedex_id`),
  ADD KEY `pokemon_id` (`pokemon_id`),
  ADD KEY `trainer_id` (`trainer_id`),
  ADD KEY `ix_Pokedex_pokedex_id` (`pokedex_id`);

--
-- Indexes for table `pokemons`
--
ALTER TABLE `pokemons`
  ADD PRIMARY KEY (`pokemon_id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `ix_Pokemons_pokemon_id` (`pokemon_id`);

--
-- Indexes for table `pokemontypes`
--
ALTER TABLE `pokemontypes`
  ADD PRIMARY KEY (`pokemon_types_id`),
  ADD KEY `pokemon_id` (`pokemon_id`),
  ADD KEY `type_id` (`type_id`),
  ADD KEY `ix_PokemonTypes_pokemon_types_id` (`pokemon_types_id`);

--
-- Indexes for table `trainers`
--
ALTER TABLE `trainers`
  ADD PRIMARY KEY (`trainer_id`,`name`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `ix_Trainers_trainer_id` (`trainer_id`);

--
-- Indexes for table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`types_id`),
  ADD UNIQUE KEY `pokemon_type` (`pokemon_type`),
  ADD KEY `ix_Types_types_id` (`types_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pokedex`
--
ALTER TABLE `pokedex`
  MODIFY `pokedex_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pokemons`
--
ALTER TABLE `pokemons`
  MODIFY `pokemon_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pokemontypes`
--
ALTER TABLE `pokemontypes`
  MODIFY `pokemon_types_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `trainers`
--
ALTER TABLE `trainers`
  MODIFY `trainer_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `types_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pokedex`
--
ALTER TABLE `pokedex`
  ADD CONSTRAINT `pokedex_ibfk_1` FOREIGN KEY (`pokemon_id`) REFERENCES `pokemons` (`pokemon_id`),
  ADD CONSTRAINT `pokedex_ibfk_2` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`trainer_id`);

--
-- Constraints for table `pokemontypes`
--
ALTER TABLE `pokemontypes`
  ADD CONSTRAINT `pokemontypes_ibfk_1` FOREIGN KEY (`pokemon_id`) REFERENCES `pokemons` (`pokemon_id`),
  ADD CONSTRAINT `pokemontypes_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `types` (`types_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
