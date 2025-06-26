-- This script list all row table
SELECT
ROW_NUMBER() OVER (...) as first_table,
name,
First_name,
Last_name,
name
FROM hbtn_0c_0
