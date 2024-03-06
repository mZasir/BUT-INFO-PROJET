

DROP TABLE IF EXISTS TableTemp;

CREATE TABLE IF NOT EXISTS TableTemp (
    country VARCHAR(100),
    year INT,
    CL INT,
    PR INT,
    status VARCHAR(2),
    region_code INT,
    region_name VARCHAR(75),
    is_ldc BOOLEAN) ;

\copy TableTemp FROM 'D:/Cours/BUT INFO1/SAE S105 (BDD)/freedom.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');



INSERT INTO region (region_code, name)
SELECT DISTINCT region_code, region_name
FROM TableTemp;

INSERT INTO country (name, is_ldc, region_code)
SELECT DISTINCT country, is_ldc, region_code
FROM TableTemp;

INSERT INTO status (status)
SELECT DISTINCT status
FROM TableTemp;

INSERT INTO freedom (id_country, year, civil_liberties, political_rights, status)
SELECT c.id_country, t.year, t.CL, t.PR, t.status
FROM TableTemp t
JOIN country c ON t.country = c.name;


