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

INSERT INTO users (name, email, password) VALUES('rafiq','rafiq@gmail.com','$2b$12$35ooP1ekrfej3W.NJz7Ku.kqlH.68zQ.og4MqkQRqxgi5zR6RNk4O');