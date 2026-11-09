# Employee Data Processing System

## Project Overview

A Python-based Employee Data Processing System that reads employee records from CSV and JSON files, validates and normalizes employee information, detects duplicate records, and generates statistical reports.

The system is integrated with a MySQL database to store valid employee records and track validation errors and duplicate records.

The project uses Object-Oriented Programming (OOP), Python's standard libraries, and MySQL Connector.

## Features

- Load employee data from CSV and JSON files.
- Validate required fields, salaries, email formats, employment status, and joining dates.
- Normalize employee names, email addresses, departments, and employment status.
- Detect duplicate employees using Employee ID or email.
- Separate valid and invalid employee records.
- Search employees by ID or name.
- Filter employees by department or employment status.
- Sort employees by salary.
- Group employees by department.
- Calculate employee statistics.
- Generate CSV and JSON reports.
- Implement a custom exception, decorator, generator, type hints, and logging.
- Perform unit testing using Python's `unittest` library.
- Connect Python to a MySQL database.
- Store valid employees in the MySQL `employees` table.
- Store validation errors and duplicate records in the MySQL `errors` table.
- Handle database operations using cursors, transactions, commits, and rollbacks.
- Prevent repeated insertion of existing employees and duplicate error records.
- Manage database connections using a dedicated `DatabaseManager` class.

## Project Structure

```text
Hari-Backend-Training/
├── .gitignore
├── requirements.txt
└── Task1/
    ├── main.py
    ├── database.py
    ├── schema.sql
    ├── test_main.py
    ├── employees.csv
    ├── employees.json
    └── README.md
```

Output files such as `valid_employees.csv`, `invalid_employees.json`, `duplicates.json`, `statistics.json`, and `app.log` are generated locally when the program runs.

## OOP Structure

The system includes five main classes:

- **EmployeeFileHandler:** Reads employee data and saves valid employee records.
- **EmployeeValidator:** Validates employee information and separates valid and invalid records.
- **EmployeeProcessor:** Handles normalization, duplicate detection, searching, filtering, sorting, and grouping.
- **EmployeeStatistics:** Calculates employee statistics and salary information.
- **DatabaseManager:** Manages MySQL connections, inserts valid employees, stores validation errors and duplicates, handles database errors, and closes connections.

## MySQL Database Integration

The system uses MySQL to store processed employee data.

### Database

**Database Name:** `employee_management`

The database contains two tables.

### 1. employees

Stores employee records that successfully pass validation.

| Column | Data Type |
|---|---|
| Employee_ID | INT (Primary Key) |
| Full_name | VARCHAR(100) |
| Email | VARCHAR(150), UNIQUE |
| Department | VARCHAR(100) |
| Salary | DECIMAL(10,2) |
| Joining_date | DATE |
| Employment_Status | VARCHAR(20) |

### 2. errors

Stores validation errors and duplicate employee records.

| Column | Data Type |
|---|---|
| Error_ID | INT, AUTO_INCREMENT (Primary Key) |
| Employee_ID | VARCHAR(50) |
| Error_Type | VARCHAR(100) |
| Error_Message | TEXT |

### Database Operations

The `DatabaseManager` class provides four main methods:

- `connect()` — Establishes a connection to MySQL.
- `insert_employee()` — Inserts valid employee records into the database.
- `insert_error()` — Stores validation errors and duplicate records.
- `close()` — Closes the database connection.

The system uses parameterized SQL queries with `%s` placeholders and handles database errors using `try`, `except`, `commit()`, and `rollback()`.

### Duplicate Handling

- `INSERT IGNORE` is used to skip existing employee records.
- `NOT EXISTS` is used to avoid inserting identical error records multiple times.
- Database constraints such as `PRIMARY KEY` and `UNIQUE` help maintain data integrity.

### 4. Run the Application

From the repository root directory:

```bash
python Task1/main.py
```

The application reads employee records, processes and validates the data, generates output reports, and stores the results in MySQL.

## Running Unit Tests

From the `Task1` directory, run:

```bash
python -m unittest test_main.py
```

The tests cover valid, negative, and non-numeric salary values.

## Output Files

| File | Description |
|---|---|
| valid_employees.csv | Valid employee records |
| invalid_employees.json | Invalid employee records with error messages |
| duplicates.json | Duplicate employee records |
| statistics.json | Employee counts, salary statistics, department counts, and top five highest-paid employees |
| app.log | Logged program events and file errors |

## Database Results

During testing, the system processed nine employee records from CSV and JSON files.

- **4 valid employees** stored in the `employees` table.
- **4 validation errors** stored in the `errors` table.
- **1 duplicate record** logged in the `errors` table.

Repeated execution was tested to verify that existing employee records and identical errors were not inserted again.

## Technologies

- Python
- Object-Oriented Programming (OOP)
- MySQL
- mysql-connector-python
- SQL
- CSV and JSON
- pathlib
- logging
- unittest
- Git and GitHub

## Author

Donia Awni Said

Backend Training Project
