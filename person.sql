-- -- Drop only relevant tables
-- DROP TABLE IF EXISTS person CASCADE;
-- DROP TABLE IF EXISTS person_type CASCADE;

-- Create person_type
--CREATE TABLE person_type (
--    id SERIAL PRIMARY KEY,
--    type_name VARCHAR(50) UNIQUE NOT NULL
--);



-- Seed data
--INSERT INTO person_type (type_name) VALUES ('student'), ('pracownik'), ('HUR HUR HUR');

--INSERT INTO person (first_name, last_name, person_type_id, age) VALUES 
--    ('El', 'Primo', 1, 21), 
--    ('Jan', 'Kowalski', 2, 45), 
--    ('Miłosz', 'Kowalski', 2, 33), 
--    ('Mati', 'Krzyśpiuk', 1, 19),
--    ('Freddy', 'Fazbear', 3, 999), 
--    ('Adrian', 'Bojno', 1, 23),
--    ('Madera', 'Pomidorowa', 1, 24);

CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    person_type_id INT NOT NULL,
    age INT NOT NULL,
	FOREIGN KEY (person_type_id) REFERENCES person_type(id) ON DELETE RESTRICT,
    latitude FLOAT,  
    longitude FLOAT
);

