-- This script create database and user 
SELECT
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE IF NOT EXISTS USER 'user_0d_2'@'localhost';
GRANT SELECT PRIVILEGE ON *.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
