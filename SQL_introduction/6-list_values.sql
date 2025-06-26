-- This script list all row table
SELECT
ROW_NUMBER() OVER (First_name, Last_name, name) as first_table,
First_name,
Last_name,
name
FROM hbtn_0c_0
