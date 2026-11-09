import csv
import datetime
import json
from database import DatabaseManager
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
import logging
logging.basicConfig(
    filename=BASE_DIR / "app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
#decoroter
def  log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info("Function started")
        result = func(*args, **kwargs)
        logging.info("Function finished")
        return result
    return wrapper
#custom Exception
class EmployeeError(Exception):
    pass
################################################
class EmployeeFileHandler:
    @log_execution
    def load_employees(self):
        employees = []
        file_path = BASE_DIR / "employees.csv"

        try:
            with open(file_path, 'r', encoding='utf-8-sig', newline='') as file:
                r = csv.DictReader(file)
                employees = [read for read in r]

            if not employees:
                raise EmployeeError("no employee found")

        except FileNotFoundError:
            logging.error("file not found")
        except EmployeeError as error:
            print(f"employee error : {error}")
        return employees
    ############################################
    def load_json_employees(self , file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
          employees = json.load(file)
        return employees

    ################################################
    # valid_employees.csv
    def save_valid_employees(self, valid_employees):
        with open('valid_employees.csv', 'w', newline='') as file:
            fieldnames = [
                "Employee_ID",
                "Full_name",
                "Email",
                "Department",
                "Salary",
                "Joining_date",
                "Employment_Status"
            ]
            w = csv.DictWriter(file, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(valid_employees)

################################################
class EmployeeValidator:

    def validate_salary(self, salary:str)->list[str]:
        errors = []

        try:
            salary = float(salary)

            if salary <= 0:
                errors.append("Invalid salary")

        except (ValueError, TypeError):
            errors.append("Salary must be a number")

        return errors

    ################################################
    def validate_email(self, email:str)->list[str]:
        if not email:
            return ["Invalid email format"]
        if "@" not in email or "." not in email:
            return ["Invalid email format"]

        return []

    ################################################
    def validate_status(self, status:str)->list[str]:
        if status not in ["Active", "Inactive"]:
            return ["Invalid employment status"]
        return []

    ################################################
    def joining_dates(self, date:str)->list[str]:
        errors = []
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except (ValueError, TypeError):
            errors.append("Invalid date format. Expected YYYY-MM-DD.")

        return errors

    ################################################
    def validate_required_fields(self, employee):
        required_fields = ["Employee_ID", "Full_name", "Email", "Department", "Salary", "Joining_date", "Employment_Status"]
        errors = []

        for field in required_fields:
            if not str(employee.get(field) or "").strip():
                errors.append(f"{field} is required")

        return errors

    ################################################
    def separate_employees(self, employees):
        valid_employee = []
        invalid_employee = []
        for emp in employees:
            errors = self.validate_employee(emp)
            if errors:
                emp["Errors"] = errors
                invalid_employee.append(emp)
            else:
                valid_employee.append(emp)
        return valid_employee, invalid_employee

    ################################################
    def validate_employee(self, employee):
        errors = []

        errors.extend(self.validate_required_fields(employee))
        errors.extend(self.validate_salary(employee.get("Salary")))
        errors.extend(self.validate_email(employee.get("Email")))
        errors.extend(self.validate_status(employee.get("Employment_Status")))
        errors.extend(self.joining_dates(employee.get("Joining_date")))
        # errors.extend(separate_employees(employee.))
        return errors

################################################

class EmployeeProcessor:

    def normalize_employees(self, employees):
        for emp in employees:
            emp["Employee_ID"] = str(emp.get("Employee_ID") or "").strip()
            emp["Full_name"] = " ".join(str(emp.get("Full_name") or "").split()).title()
            emp["Email"] = str(emp.get("Email") or "").strip().lower()
            emp["Department"] = str(emp.get("Department") or "").strip().title()
            emp["Joining_date"] = str(emp.get("Joining_date") or "").strip()
            emp["Employment_Status"] = str(emp.get("Employment_Status") or "").strip().capitalize()

        return employees

    ################################################
    def duplicate_emp(self, employees):
        seen_ids = set()
        seen_emails = set()
        duplicate = []
        unique_employees = []
        for emp in employees:
            emp_id = emp.get("Employee_ID")
            email = emp.get("Email")
            # if emp_id in seen_ids or email in seen_emails: add it in duplicat
            if emp_id in seen_ids or email in seen_emails:
                duplicate.append(emp)
            # if not, add it in the seen_set
            else:
                seen_ids.add(emp_id)
                seen_emails.add(email)
                unique_employees.append(emp)
        return unique_employees, duplicate

    ################################################
    def group_by_department(self, employees):
        department_groups = {}

        for emp in employees:
            department = emp.get("Department")
            if department not in department_groups:
                department_groups[department] = []
            department_groups[department].append(emp)

        return department_groups

    ################################################
    def search_employee(self, employees, keyword):
        keyword = str(keyword).strip().lower()
        results = []

        for emp in employees:
            if (keyword == str(emp["Employee_ID"]).lower()
                    or keyword in emp["Full_name"].lower()):
                results.append(emp)

        return results

    ################################################
    def sort_by_salary(self, employees):
        return sorted(
            employees,
            key=lambda emp: float(emp["Salary"]),
            reverse=True
        )

    ################################################
    def filter_employees(self, employees, department=None, status=None):
        filtered = employees

        if department:
            filtered = [emp for emp in filtered if emp["Department"].lower() == department.lower()]

        if status:
            filtered = [emp for emp in filtered if emp["Employment_Status"].lower() == status.lower()]

        return filtered
    # generator
    def employee_generator(self , employees):
        for emp in employees:
            yield emp
###############################################

class EmployeeStatistics:

    def __init__(self, processor):
        self.processor = processor

    def calculate_statistics(self, valid_employees, invalid_employees, duplicates):
        stats = {}
        stats["Valid Employees"] = len(valid_employees)
        stats["Invalid Employees"] = len(invalid_employees)
        stats["Duplicate Employees"] = len(duplicates)
        salaries = [float(emp["Salary"]) for emp in valid_employees if emp.get("Salary")]
        len(salaries)
        sum(salaries)
        min_salary = min(salaries) if salaries else 0
        max_salary = max(salaries) if salaries else 0
        avg_salary = sum(salaries) / len(salaries) if salaries else 0

        stats["Average Salary"] = avg_salary
        stats["Minimum Salary"] = min_salary
        stats["Maximum Salary"] = max_salary
        sorted_employees = self.processor.sort_by_salary(valid_employees)
        # Let's get the top 5 highest-paid employees (Listed slicing)
        stats["Top 5 highest-paid employees "] = sorted_employees[:5]
        # Group employees by department and count them
        groups = self.processor.group_by_department(valid_employees)
        department_counts = {}
        for dept in groups:
            department_counts[dept] = len(groups[dept])
        stats["Employee count per department"] = department_counts
        # Active vs. inactive employees
        active_count = 0
        inactive_count = 0
        for emp in valid_employees:
            if emp.get("Employment_Status") == "Active":
                active_count += 1
            elif emp.get("Employment_Status") == "Inactive":
                inactive_count += 1
        stats["Active Employees"] = active_count
        stats["Inactive Employees"] = inactive_count
        # Total employees
        stats["Total Employees"] = len(valid_employees) + len(invalid_employees) + len(duplicates)

        return stats

############################################
#invalid_employees.json
def save_invalid_employees(invalid_employees) :
    with open('invalid_employees.json', 'w' ,encoding="utf-8") as file:
       json.dump(invalid_employees, file, indent=4, ensure_ascii=False)
############################################
#duplicates.json
def save_duplicates(duplicates) :
     with open('duplicates.json', 'w') as file:
        r = json.dump(duplicates, file, indent=4, ensure_ascii=False)
#############################################
def save_statistics(statistics):
    with open('statistics.json', 'w') as file:
        json.dump(statistics, file, indent=4, ensure_ascii=False)
################################

def main():
    file_handler = EmployeeFileHandler()
    employees = file_handler.load_employees()
    json_employees = file_handler.load_json_employees(BASE_DIR / "employees.json")
    employees.extend(json_employees)
    processor = EmployeeProcessor()
    employees = processor.normalize_employees(employees)
    unique_employees, duplicates = processor.duplicate_emp(employees)
    validator = EmployeeValidator()
    valid_employees, invalid_employees = validator.separate_employees(unique_employees)
    file_handler.save_valid_employees(valid_employees)
    save_invalid_employees(invalid_employees)
    save_duplicates(duplicates)
    statistics_calculator = EmployeeStatistics(processor)
    statistics = statistics_calculator.calculate_statistics(
        valid_employees,
        invalid_employees,
        duplicates
    )
    # 5. Save statistics
    save_statistics(statistics)

    for emp in processor.employee_generator(valid_employees):
        print(emp["Full_name"])


    db = DatabaseManager()
    db.connect()
    for emp in valid_employees:
        db.insert_employee(emp)
    for emp in invalid_employees:
      for error in emp["Errors"]:
        db.insert_error(emp["Employee_ID"], "Validation", error)
    for dup in duplicates:
      db.insert_error(
        dup["Employee_ID"],
        "Duplicate",
        "Duplicate employee ID or email"
    )
    db.close()
if __name__ == "__main__":
    main()
