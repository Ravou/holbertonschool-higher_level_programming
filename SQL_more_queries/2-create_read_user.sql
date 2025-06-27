-- This script create database and user 
SELECT
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT PRIVILEGE ON *.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
