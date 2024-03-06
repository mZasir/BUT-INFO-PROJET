-- MySQL Script generated by MySQL Workbench
-- Mon Jan 22 22:47:36 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
SHOW WARNINGS;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `COUNTRY`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `COUNTRY` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `COUNTRY` (
  `id_country` INT NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `is_ldc` TINYINT NULL DEFAULT NULL,
  `region_code` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_country`),
  CONSTRAINT ``
    FOREIGN KEY (`region_code`)
    REFERENCES `REGION` (`region_code`));

SHOW WARNINGS;
CREATE INDEX ON `COUNTRY` (`region_code` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `FREEDOM`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FREEDOM` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `FREEDOM` (
  `id_country` INT NULL DEFAULT NULL,
  `year` INT NULL DEFAULT NULL,
  `civil_liberties` INT NULL DEFAULT NULL,
  `political_rights` INT NULL DEFAULT NULL,
  `status` VARCHAR(2) NULL DEFAULT NULL,
  PRIMARY KEY (`id_country`, `year`),
  CONSTRAINT ``
    FOREIGN KEY (`id_country`)
    REFERENCES `COUNTRY` (`id_country`),
  CONSTRAINT ``
    FOREIGN KEY (`status`)
    REFERENCES `STATUS` (`status`));

SHOW WARNINGS;
CREATE INDEX ON `FREEDOM` (`status` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX ON `FREEDOM` (`status` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `REGION`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `REGION` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `REGION` (
  `region_code` INT NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`region_code`));

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `STATUS`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `STATUS` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `STATUS` (
  `status` VARCHAR(2) NULL DEFAULT NULL,
  PRIMARY KEY (`status`));

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
