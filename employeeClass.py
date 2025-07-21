class Employee:
    emp_id = 1
    emp_name = "Name"
    emp_salary = 0
    emp_department = "Department Name"

    def print_employee_details(self):
        print("Employee ID is: " + str(self.emp_id) + ", Employee Name is: " + self.emp_name + ", Employee Salary is: " + str(self.emp_salary) + ", Employee Department is: " + self.emp_department)

    def emp_assign_department(self, department):
        self.emp_department = department

    def calculate_emp_salary(self, salary, hours_worked):
        self.emp_salary = salary * hours_worked
