CREATE TABLE nodes (
  id serial PRIMARY KEY,
  osmid bigint,
  long float,
  lat float
);

CREATE TABLE orders (
  id serial PRIMARY KEY,
  date_time timestamp,
  from_node integer REFERENCES nodes(id),
  to_node integer REFERENCES nodes(id),
  distance float,
  cost int,
  rating int
);  

-- Заполняем ноды
COPY nodes(osmid, long, lat)
FROM '/docker-entrypoint-initdb.d/nodes.csv'
DELIMITER ','
CSV HEADER;