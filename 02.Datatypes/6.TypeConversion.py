## Implicit type conversion
# Addition of two numbers
num1 = 12                  # datatype is int
num2 = 10.7                # datatype is float
addition = num1 + num2
print(addition)            # Output : 22.7
print(type(addition))      # Output : float

## Explicit type conversion
# Addition of two numbers - user input is considered str by default
num1 = input("Enter the first number : ")    # Try with 6
num2 = input("Enter the second number : ")   # Try with 8
addition = num1 + num2
print(addition)                              # Output : 68

## Revised after type conversion
# Addition of two numbers
num1 = int(input("Enter the first number : "))    # Try with 6
num2 = int(input("Enter the second number : "))   # Try with 8
addition = num1 + num2
print(addition)                                   # Output : 14