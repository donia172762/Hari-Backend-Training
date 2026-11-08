# Employee Data Processing System

## Project Overview

A Python-based Employee Data Processing System that reads employee records from CSV and JSON files, validates and normalizes employee information, detects duplicate records, and generates statistical reports.

The project uses Object-Oriented Programming (OOP) and Python's standard libraries.

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

## Project Structure

Task1/
├── main.py
├── test_main.py
├── employees.csv
├── employees.json
├── valid_employees.csv
├── invalid_employees.json
├── duplicates.json
├── statistics.json
├── app.log
└── README.md


## OOP Structure

The system includes four main classes:

- **EmployeeFileHandler:** Reads employee data and saves valid employee records.
- **EmployeeValidator:** Validates employee information and separates valid and invalid records.
- **EmployeeProcessor:** Handles normalization, duplicate detection, searching, filtering, sorting, and grouping.
- **EmployeeStatistics:** Calculates employee statistics and salary information.

## How to Run

Requirements: Python 3.9 or later. No third-party packages are required.

1. Place `employees.csv` and `employees.json` in the project directory.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

The program processes employee records and generates output reports.

## Running Unit Tests

Run:

```bash
python -m unittest test_main.py


The tests cover valid, negative, and non-numeric salary values.

## Output Files

| File | Description |
|---|---|
| valid_employees.csv | Valid employee records |
| invalid_employees.json | Invalid employee records with error messages |
| duplicates.json | Duplicate employee records |
| statistics.json | Employee counts, salary statistics, department counts, and top five highest-paid employees |
| app.log | Logged program events and file errors |

## Technologies

- Python
- Object-Oriented Programming
- CSV and JSON
- pathlib
- logging
- unittest

## Author

Donia Awni Said

Backend Training Project