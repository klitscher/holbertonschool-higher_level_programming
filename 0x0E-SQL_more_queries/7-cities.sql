-- Script that creates a database and a table
-- Creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Enter database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL);
