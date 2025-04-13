ATTACH DATABASE 'task2/db/company1.db' AS cp1;
ATTACH DATABASE 'task3/company2.db' AS cp2;

-- PRAGMA cp1.table_info('employees');
PRAGMA cp2.table_info('employees');

DETACH DATABASE cp1;
DETACH DATABASE cp2;