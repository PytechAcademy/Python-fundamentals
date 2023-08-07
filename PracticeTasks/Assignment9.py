def factorial_iterative(n):
    if n < 0:
        return "Factorial is undefined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Taking input from the user
num = int(input("Enter a non-negative integer: "))

# Calculating the factorial using iteration
factorial = factorial_iterative(num)

# Displaying the result
print(f"The factorial of {num} is {factorial}")
