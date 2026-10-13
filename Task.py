
import csv
import sqlite3

# Connect to the database
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Read employee data from the CSV file
with open("Employee.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames
    employees = list(reader)

# Create the table columns automatically
column_definitions = []

for column in columns:
    name = column.strip()

    if name.lower() == "id":
        column_definitions.append(f'"{name}" INTEGER PRIMARY KEY')
    elif name.lower() == "salary":
        column_definitions.append(f'"{name}" REAL')
    elif name.lower()=="join_date":
        column_definitions.append(f'"{name}" DATE')
    else:
        column_definitions.append(f'"{name}" TEXT')

# Recreate the table to avoid duplicate records on reruns
cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute(
    f"CREATE TABLE employees ({', '.join(column_definitions)})"
)

# Prepare employee data for insertion
values = []

for employee in employees:
    row = []

    for column in columns:
        value = employee[column].strip() or None

        if column.strip().lower() == "salary" and value is not None:
            value = float(value)

        row.append(value)

    values.append(row)

# Insert all employees in one batch
placeholders = ", ".join(["?"] * len(columns))

cursor.executemany(
    f"INSERT INTO employees VALUES ({placeholders})",
    values
)

conn.commit()
print(f"Loaded {len(values)} employees successfully.")

# Query 1: Count employees in each department
print("\nEmployee Count by Department:")

cursor.execute("""
    SELECT department, COUNT(*)
    FROM employees
    GROUP BY department
""")

for result in cursor.fetchall():
    print(result)

# Query 2: Find the highest-paid employee in each department
print("\nHighest Paid Employee by Department:")

cursor.execute("""
    SELECT *
    FROM employees e
    WHERE salary = (
        SELECT MAX(salary)
        FROM employees
        WHERE department = e.department
    )
    ORDER BY department
""")

for result in cursor.fetchall():
    print(result)

# Query 3: Find employees who joined within the last year
print("\nEmployees Joined in the Last Year:")

cursor.execute("""
    SELECT *
    FROM employees
    WHERE date(join_date) BETWEEN date('now', '-1 year')
                              AND date('now')
    ORDER BY date(join_date) DESC
""")

for result in cursor.fetchall():
    print(result)

# Close the database connection
conn.close()
