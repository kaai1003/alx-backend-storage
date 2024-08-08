-- create table users if not exist
-- fields: id(in), email(string), name(string)
CREATE TABLE users IF NOT EXISTS (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
