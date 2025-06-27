-- This script create server user
-- and grants all privileges on the server

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
