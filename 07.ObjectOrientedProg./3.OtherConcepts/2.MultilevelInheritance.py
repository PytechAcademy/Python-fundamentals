class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return f"Hello, I am {self.name} and I am {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, salary, dept):
        super().__init__(name, age)
        self.salary = salary
        self.dept = dept

    def employee_info(self):
        return f"I am an employee. My name is {self.name}, and I work in {self.dept} department with a salary of {self.salary}."


class EmployeeAttrition(Employee):
    def __init__(self, name, age, salary, dept, attrition):
        super().__init__(name, age, salary, dept)
        self.attrition = attrition

    def attrition_info(self):
        return f"I am an employee with attrition. My name is {self.name}, I work in {self.dept} department, and my salary is {self.salary}. Attrition rate: {self.attrition}%."


# Example usage
attrition_employee = EmployeeAttrition('Alice', 30, 60000, 'HR', 10)
print(attrition_employee.employee_info())  # Inherited method from Employee
print(attrition_employee.attrition_info())  # Method from EmployeeAttrition