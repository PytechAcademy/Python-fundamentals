class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, my name is {} and I am {} years old.".format(self.name,self.age)

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # Output: Hello, my name is Bob and I am 25 years old.