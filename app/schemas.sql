-- create database
CREATE DATABASE IF NOT EXISTS PyContacts;

-- set default database
USE PyContacts;

-- create table
CREATE TABLE IF NOT EXISTS Contacts (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);

-- insert data
INSERT INTO Contacts (name, phone) VALUES ('John Doe', '555-555-5555');
INSERT INTO Contacts (name, phone) VALUES ('Jane Doe', '555-555-5555');
