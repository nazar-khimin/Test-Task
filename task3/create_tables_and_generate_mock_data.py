from faker import Faker
import sqlite3
import random

# Setup
fake = Faker()
conn = sqlite3.connect("company2.db")
cursor = conn.cursor()

# Create schema
cursor.executescript("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    dob DATE NOT NULL,
    salary INTEGER NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(dept_id)
);
""")

# Departments
departments = [ "HR", "Engineering","Marketing", "Sales","Finance","Operations",
                "Legal","Customer Support", "Product Management","IT"]
cursor.executemany("INSERT INTO departments (dept_name) VALUES (?)", [(d,) for d in departments])

# Generate employees
def generate_employees(n: int = 100):
    employees = []
    for _ in range(n):
        full_name = fake.name()
        dob = fake.date_of_birth(minimum_age=21, maximum_age=60).isoformat()
        salary = random.randint(30000, 150000)
        department_id = random.randint(1, len(departments))
        employees.append((full_name, dob, salary, department_id))
    return employees

# Insert employees
cursor.executemany(
    "INSERT INTO employees (full_name, dob, salary, department_id) VALUES (?, ?, ?, ?)",
    generate_employees(100)
)

conn.commit()
conn.close()