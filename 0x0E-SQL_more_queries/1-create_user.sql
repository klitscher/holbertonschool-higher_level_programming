-- Script to create a new user
-- See above
CREATE USER IF NOT EXISTS 'user_0d_1'@localhost IDENTIFIED BY 'user_0d_1_pwd';

--Grants priveleges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
