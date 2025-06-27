-- This script create server user
INSERT INTO 
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
