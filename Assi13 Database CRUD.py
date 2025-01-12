import mysql.connector
import configparser
import re
from mysql.connector import IntegrityError

config = configparser.ConfigParser()
config.read('config.ini')

db_config = {
    'host': config['mysql']['host'],
    'user': config['mysql']['user'],
    'password': config['mysql']['password']
}


db = mysql.connector.connect(**db_config)
cursor = db.cursor()

def create_database(database_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    cursor.execute(f"USE {database_name}")

database_name = config['mysql']['database']
create_database(database_name)

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        dept_id INT AUTO_INCREMENT PRIMARY KEY,
        dept_name VARCHAR(50),
        location VARCHAR(50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        empid INT AUTO_INCREMENT PRIMARY KEY,
        empname VARCHAR(100),
        dept_id INT,
        salary DECIMAL(10, 2),
        FOREIGN KEY (dept_id) REFERENCES Department(dept_id) ON DELETE CASCADE
    )
    """)

create_tables()

def validate_integer(input_value, field_name):
    if not input_value.isdigit():
        print(f"Invalid {field_name}. Please enter a valid number.")
        return None
    return int(input_value)

def validate_name(name):
    pattern = r"^[a-zA-Z .'-]+$"
    if not re.match(pattern, name):
        print("Invalid name.")
        return None
    return name

def add_department():
    dept_name = input("Enter Department Name: ")
    if not dept_name:
        print("Department Name cannot be empty.")
        return

    location = input("Enter Location: ")
    if not location:
        print("Location cannot be empty.")
        return

    cursor.execute(
        "INSERT INTO Department (dept_name, location) VALUES (%s, %s)",
        (dept_name, location)
    )
    db.commit()
    print("Department added successfully!")

def add_employee():
    empname = input("Enter Employee Name: ")
    empname = validate_name(empname)
    if empname is None:
        return

    dept_name = input("Enter Department Name: ")
    cursor.execute("SELECT dept_id FROM Department WHERE dept_name = %s", (dept_name,))
    dept = cursor.fetchone()

    if not dept:
        print("Department not found.")
        return

    salary = input("Enter Salary: ")
    try:
        salary = float(salary)
    except ValueError:
        print("Invalid Salary. Please enter a valid number.")
        return

    dept_id = dept[0]
    cursor.execute(
        "INSERT INTO Employee (empname, dept_id, salary) VALUES (%s, %s, %s)",
        (empname, dept_id, salary)
    )
    db.commit()
    print("Employee added successfully!")

def delete_department():
    dept_name = input("Enter Department Name to delete: ")
    cursor.execute("DELETE FROM Employee WHERE dept_id = (SELECT dept_id FROM Department WHERE dept_name = %s)", (dept_name,))
    cursor.execute("DELETE FROM Department WHERE dept_name = %s", (dept_name,))
    db.commit()
    print(f"Department '{dept_name}' and related employees deleted successfully!")

def delete_employee():
    empid = input("Enter Employee ID to delete: ")
    empid = validate_integer(empid, "Employee ID")
    if empid is None:
        return

    cursor.execute("DELETE FROM Employee WHERE empid = %s", (empid,))
    db.commit()
    print(f"Employee ID {empid} deleted successfully!")

def search_department():
    dept_name = input("Enter Department Name to search: ")
    cursor.execute("SELECT * FROM Department WHERE dept_name = %s", (dept_name,))
    result = cursor.fetchone()

    if result:
        print(f"Department Details: {result}")
    else:
        print(f"Department '{dept_name}' not found.")

def update_department():
    dept_name = input("Enter Department Name to update: ")
    cursor.execute("SELECT dept_id FROM Department WHERE dept_name = %s", (dept_name,))
    result = cursor.fetchone()

    if result:
        dept_id = result[0]
        new_name = input("Enter new Department Name: ")
        new_location = input("Enter new Location: ")

        cursor.execute(
            "UPDATE Department SET dept_name = %s, location = %s WHERE dept_id = %s",
            (new_name, new_location, dept_id)
        )
        db.commit()
        print(f"Department '{dept_name}' updated successfully!")
    else:
        print(f"Department '{dept_name}' not found.")

def update_employee():
    empid = input("Enter Employee ID to update: ")
    empid = validate_integer(empid, "Employee ID")
    if empid is None:
        return

    cursor.execute("SELECT * FROM Employee WHERE empid = %s", (empid,))
    result = cursor.fetchone()

    if result:
        new_name = input("Enter new Employee Name: ")
        new_name = validate_name(new_name)
        if new_name is None:
            return

        new_salary = input("Enter new Salary: ")
        try:
            new_salary = float(new_salary)
        except ValueError:
            print("Invalid Salary. Please enter a valid number.")
            return

        cursor.execute(
            "UPDATE Employee SET empname = %s, salary = %s WHERE empid = %s",
            (new_name, new_salary, empid)
        )
        db.commit()
        print(f"Employee ID {empid} updated successfully!")
    else:
        print(f"Employee ID {empid} not found.")

def generate_reports():
    print("Select a report type:")
    print("1. Employees with Salary Above a Limit")
    print("2. Employee Count in Each Department")

    report_type = input("Enter your choice (1/2): ")

    if report_type == '1':
        salary_limit = input("Enter the salary limit (e.g., 50000): ")

        try:
            salary_limit = float(salary_limit)
            cursor.execute("SELECT empname, salary FROM Employee WHERE salary > %s", (salary_limit,))
            results = cursor.fetchall()

            if results:
                print(f"\nEmployees with salary above {salary_limit}:")
                for row in results:
                    print(f"Employee: {row[0]}, Salary: {row[1]}")
            else:
                print(f"No employees found with salary above {salary_limit}.")
        except ValueError:
            print("Invalid salary input. Please enter a valid number.")

    elif report_type == '2':
        print("\nGenerating report for employee count in each department...")
        cursor.execute("""
        SELECT d.dept_name, COUNT(e.empid) AS num_employees
        FROM Department d
        LEFT JOIN Employee e ON d.dept_id = e.dept_id
        GROUP BY d.dept_name
        """)
        results = cursor.fetchall()

        if results:
            print("\nEmployee count in each department:")
            for row in results:
                print(f"Department: {row[0]}, Number of Employees: {row[1]}")
        else:
            print("No departments found.")

    else:
        print("Invalid input. Please choose either 1 or 2.")
def select_data():
    print("Select what to view:")
    print("1. View Departments")
    print("2. View Employees")
    choice = input("Enter your choice: ")

    if choice == '1':
        cursor.execute("SELECT * FROM Department")
        departments = cursor.fetchall()
        if departments:
            print("\nDepartments:")
            print("|| Dept ID || Dept Name || Location ||")
            print("||---------||-----------||----------||")
            for dept in departments:
                print(f"|| {dept[0]}      || {dept[1]}      || {dept[2]} ||")
        else:
            print("No departments found.")
    elif choice == '2':
        cursor.execute("SELECT * FROM Employee")
        employees = cursor.fetchall()
        if employees:
            print("\nEmployees:")
            print("|| Emp ID || Emp Name || Dept ID || Salary ||")
            print("||--------||----------||---------||--------||")
            for emp in employees:
                print(f"|| {emp[0]}      || {emp[1]}     || {emp[2]}     || {emp[3]} ||")
        else:
            print("No employees found.")
    else:
        print("Invalid choice.")




def menu():
    while True:
        print("\nMenu:")
        print("1. Add Department")
        print("2. Add Employee")
        print("3. Delete Department")
        print("4. Delete Employee")
        print("5. Search Department")
        print("6. Update Department")
        print("7. Update Employee")
        print("8. View Data")
        print("9. Generate Reports")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_department()
        elif choice == '2':
            add_employee()
        elif choice == '3':
            delete_department()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            search_department()
        elif choice == '6':
            update_department()
        elif choice == '7':
            update_employee()
        elif choice == '8':
            select_data()
        elif choice == '9':
            generate_reports()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
cursor.close()
db.close()

