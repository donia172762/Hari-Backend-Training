import mysql.connector
import os

class DatabaseManager:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password=os.getenv("MYSQL_PASSWORD"),
                database="employee_management"
            )

            if self.connection.is_connected():
                print("Connected successfully!")

        except mysql.connector.Error as error:
            print("Database connection failed:", error)

    def insert_employee(self, employee):
         cursor = self.connection.cursor()
         self.insert_employee
         sql = "INSERT IGNORE INTO employees (Employee_ID, Full_name, Email, Department, Salary, Joining_date, Employment_Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
         valuse = (
             employee["Employee_ID"],
             employee["Full_name"],
             employee["Email"],
             employee["Department"],
             employee["Salary"],
             employee["Joining_date"],
             employee["Employment_Status"],
         )
         try :
            cursor.execute(sql , valuse)
            self.connection.commit()
         except mysql.connector.IntegrityError as error :
             self.connection.rollback()
             print("Database integrity error:", error)
         finally:
            cursor.close()
    def insert_error(self, employee_id, error_type, error_message):
     cursor = self.connection.cursor()

     sql = """
        INSERT INTO errors (Employee_ID, Error_Type, Error_Message)
        SELECT %s, %s, %s
        WHERE NOT EXISTS (
            SELECT 1 FROM errors
            WHERE Employee_ID <=> %s
            AND Error_Type = %s
            AND Error_Message = %s
        )
    """

     values = (
        employee_id,
        error_type,
        error_message,
        employee_id,
        error_type,
        error_message
    )
     try :
            cursor.execute(sql , values)
            self.connection.commit()
     except mysql.connector.Error as error :
                self.connection.rollback()
                print("Database error:", error)
     finally:
            cursor.close()
    def close(self):
      if self.connection and self.connection.is_connected():
         self.connection.close()
if __name__ == "__main__":
    db = DatabaseManager()
    db.connect()