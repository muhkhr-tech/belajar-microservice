CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  selling_price INTEGER NOT NULL,
  purchase_price INTEGER NOT NULL,
  stock INTEGER NOT NULL
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL
);

INSERT INTO users (name, email, password) VALUES('rafiq','rafiq@gmail.com','123');