-- This script list all row table
SELECT
ROW_NUMBER() OVER (ORDER BY id) AS row_num,
id,
name
FROM first_table;
