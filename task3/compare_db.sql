ATTACH DATABASE 'task2/db/company1.db' AS cp1;
ATTACH DATABASE 'task3/db/company2.db' AS cp2;

SELECT
    id,
    name,
    date_of_birth,
    salary,
    department_id
FROM cp1.employees
EXCEPT
SELECT
    emp_id,
    full_name,
    dob,
    salary,
    department_id
FROM cp2.employees

UNION ALL

SELECT
    emp_id,
    full_name,
    dob,
    salary,
    department_id
FROM cp2.employees
EXCEPT
SELECT
    id,
    name,
    date_of_birth,
    salary,
    department_id
FROM cp1.employees;

DETACH DATABASE cp1;
DETACH DATABASE cp2;