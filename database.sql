-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema certificacion_1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema certificacion_1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `certificacion_1` DEFAULT CHARACTER SET utf8 ;
USE `certificacion_1` ;

-- -----------------------------------------------------
-- Table `certificacion_1`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `certificacion_1`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `certificacion_1`.`peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `certificacion_1`.`peliculas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `director` VARCHAR(255) NULL,
  `sinopsis` TEXT(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`, `usuario_id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  INDEX `fk_peliculas_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_peliculas_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `certificacion_1`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `certificacion_1`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `certificacion_1`.`comentarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comentario` TEXT(300) NULL,
  `usuario_id` INT NOT NULL,
  `pelicula_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `usuario_id`, `pelicula_id`),
  INDEX `fk_usuarios_has_peliculas_peliculas1_idx` (`pelicula_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_peliculas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_peliculas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `certificacion_1`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_peliculas_peliculas1`
    FOREIGN KEY (`pelicula_id`)
    REFERENCES `certificacion_1`.`peliculas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
