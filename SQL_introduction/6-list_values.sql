-- This script list all row table
SELECT
ROW_NUMBER() OVER (...) as first_table,
id INT,
name VARCHAR(256)
FROM hbtn_0c_0
