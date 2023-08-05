## Positional and keyword arguments
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")
greet("Alice", 30)
# Output: Hello, Alice. You are 30 years old.
greet(age=30, name="Bob")
# Output: Hello, Bob. You are 30 years old.

## Defualt and Non-default arguments
def greet(name, age=18):
  print(f"Hello, {name}. You are {age} years old.")
greet("Alice")
# Output: Hello, Alice. You are 18 years old.
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")
greet("Alice")
# This will raise an error as both arguments are required. Comment line 21 to run next code

## Arbitrary arguments
## positional arguments as sequence
def sum_values(*args):
    total = sum(args)
    return total

print(sum_values(10, 20, 30))
# Output: 60

## Keyword arguments
def print_values(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_values(a=1, b=2, c=3)
# Output: a : 1
#         b : 2
#         c : 3
