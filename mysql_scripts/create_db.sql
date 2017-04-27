# run me with mysql --force -u root -p < create_db.sql

CREATE DATABASE `saconfigdemodb`;

CREATE USER 'saconfigdemouser'@'localhost' IDENTIFIED BY 'secret';
GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE, SHOW VIEW, CREATE, DROP, ALTER, INDEX, CREATE VIEW, CREATE TEMPORARY TABLES
ON saconfigdemodb.* TO 'saconfigdemouser'@'localhost';

FLUSH PRIVILEGES;
