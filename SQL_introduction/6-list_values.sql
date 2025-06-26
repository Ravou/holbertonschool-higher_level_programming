-- This script list all row table
SELECT
ROW_NUMBER() OVER (id, name) + 3,
First_name,
Last_name,
name
FROM hbtn_0c_0
