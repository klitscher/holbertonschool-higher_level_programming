-- Script that creates a database and a table
-- Creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Enter database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
