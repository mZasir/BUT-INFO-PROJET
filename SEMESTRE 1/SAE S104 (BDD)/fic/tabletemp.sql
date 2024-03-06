

CREATE TABLE IF NOT EXISTS TableTemp (
    country VARCHAR(100),
    year INT,
    CL INT,
    PR INT,
    status VARCHAR(2),
    region_code INT,
    region_name VARCHAR(75),
    is_ldc INT) ;


\copy TableTemp FROM 'D:/Cours/BUT INFO1/SAE S105 (BDD)/freedom.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');

