CREATE TABLE houses (
    house text PRIMARY KEY,
    head text
);

CREATE TABLE students1 (
    id INTEGER PRIMARY KEY,
    studentname text NOT NULL
);

CREATE TABLE housea (
    id INTEGER ,
    house TEXT ,
    FOREIGN KEY (id) REFERENCES students1(id),
    FOREIGN KEY (house) REFERENCES houses(house)
);