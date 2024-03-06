CREATE TABLE REGION (
    region_code INT PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE STATUS (
    status VARCHAR(2) PRIMARY KEY
);

CREATE TABLE COUNTRY (
    id_country SERIAL PRIMARY KEY,
    name VARCHAR(255),
    is_ldc BOOLEAN,
    region_code INT REFERENCES REGION(region_code)
);

CREATE TABLE FREEDOM (
    id_country INT REFERENCES COUNTRY(id_country),
    year INT,
    civil_liberties INT,
    political_rights INT,
    status VARCHAR(2) REFERENCES STATUS(status),
    PRIMARY KEY (id_country, year)
);
