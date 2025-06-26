-- This script list all row table
SELECT
ROW_NUMBER() OVER () as id ,
id,
name
FROM first_table;
