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


person = Person('Alice', 25)
print(person.intro())  # Output: Hello, I am Alice and I am 25 years old.

employee = Employee('Bob', 30, 50000, 'IT')
print(employee.intro())  # Output: Hello, I am Bob and I am 30 years old.
print(
    employee.employee_info())  # Output: I am an employee. My name is Bob, and I work in IT department with a salary of 50000.