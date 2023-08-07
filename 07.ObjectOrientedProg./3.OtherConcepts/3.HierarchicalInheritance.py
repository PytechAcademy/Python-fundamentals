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


class Student(Person):
    def __init__(self, name, age, grade, type):
        super().__init__(name, age)
        self.grade = grade
        self.type = type

    def student_info(self):
        return f"I am a student. My name is {self.name}, I am {self.age} years old, studying in grade {self.grade} as a {self.type} student."


# Example usage
student = Student('John', 18, '12th', 'Full-time')
print(student.intro())  # Inherited method from Person
print(student.student_info())  # Method from Student