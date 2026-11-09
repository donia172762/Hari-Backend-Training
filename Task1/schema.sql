CREATE DATABASE IF NOT EXISTS employee_management;

USE employee_management;

CREATE TABLE IF NOT EXISTS employees (
    Employee_ID INT PRIMARY KEY,
    Full_name VARCHAR(100) NOT NULL,
    Email VARCHAR(150) UNIQUE NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    Joining_date DATE NOT NULL,
    Employment_Status VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS errors (
    Error_ID INT AUTO_INCREMENT PRIMARY KEY,
    Employee_ID VARCHAR(50),
    Error_Type VARCHAR(100) NOT NULL,
    Error_Message TEXT NOT NULL
);