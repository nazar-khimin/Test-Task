ATTACH DATABASE 'task2/db/company1.db' AS c1;
ATTACH DATABASE 'task3/db/company2.db' AS c2;

-- Count rows in both tables
-- SELECT
--     (SELECT COUNT(*) FROM c1.employees) AS company1_count,
--     (SELECT COUNT(*) FROM c2.employees) AS company2_count;

--- Compare from company1 to company2
SELECT
    c1e.*,
    c2e.*
FROM c1.employees c1e
LEFT JOIN c2.employees c2e ON c1e.name = c2e.full_name
WHERE c2e.full_name IS NULL
   OR c1e.date_of_birth != c2e.dob
   OR c1e.salary != c2e.salary
   OR c1e.department_id != c2e.department_id

UNION ALL

-- Compare from company2 to company1
SELECT
    c1e.*,
    c2e.*
FROM c2.employees c2e
LEFT JOIN c1.employees c1e ON c2e.full_name = c1e.name
WHERE c1e.name IS NULL
   OR c1e.date_of_birth != c2e.dob
   OR c1e.salary != c2e.salary
   OR c1e.department_id != c2e.department_id;

DETACH DATABASE c1;
DETACH DATABASE c2;