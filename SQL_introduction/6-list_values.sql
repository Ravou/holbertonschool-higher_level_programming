-- This script list all row table
SELECT
ROW_NUMBER() OVER (),
id,
name
FROM first_table;
