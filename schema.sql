-- Drop groups table if exists
DROP TABLE IF EXISTS groups;

-- Create the table groups
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    member1 TEXT,
    member2 TEXT,
    member3 TEXT,
    member4 TEXT,
    member5 TEXT
);

