-- This script list all row table
SELECT
ROW_NUMBER() OVER () AS row_num,
id,
name
FROM first_table;
