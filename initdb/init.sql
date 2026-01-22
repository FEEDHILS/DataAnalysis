CREATE TABLE nodes (
  id bigint PRIMARY KEY,
  long float,
  lat float
);

CREATE TABLE orders (
  id serial PRIMARY KEY,
  date_time timestamp,
  from_node bigint REFERENCES nodes(id),
  to_node bigint REFERENCES nodes(id),
  distance float,
  cost int,
  rating int
);  

-- Заполняем ноды
COPY nodes(id, long, lat)
FROM '/docker-entrypoint-initdb.d/nodes.csv'
DELIMITER ','
CSV HEADER;