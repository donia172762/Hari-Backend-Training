import unittest
from main import EmployeeValidator

class TestEmployeeValidator(unittest.TestCase):

    def test_valid_salary(self):
        validator = EmployeeValidator()
        result = validator.validate_salary(5000)
        self.assertEqual(result,[])
    def test_negative_salary(self):
         validator = EmployeeValidator()
         result = validator.validate_salary(-1000)
         self.assertEqual(result,["Invalid salary"])
    def test_Invalid_salary(self):
            validator = EmployeeValidator()
            result = validator.validate_salary("hello")
            self.assertEqual(result,["Salary must be a number"])
         