## Cubic function
X = lambda x: x**3
print(X(9))  # Output: 729

## Multiplication table
M = lambda x, y: x * y
for i in range(1, 11):
    print(M(4, i))

##Functional Programming using Lambda Functions

# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

# Function to perform an operation on each element of the list
def apply_operation(operation, num_list):
    return [operation(num) for num in num_list]

# Using lambda functions for different operations
# Square each element in the list
squared_numbers = apply_operation(lambda x: x**2, numbers)
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

## Lambda with map, reduce and filter
# map to find square of list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# filter to extract even numbers from list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# reduce to find product of numbers in list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)