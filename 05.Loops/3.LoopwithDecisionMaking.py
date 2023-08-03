# Using a while loop and decision-making to find the sum of even numbers from 1 to 10
n = 1
sum_even = 0

while n <= 10:
    if n % 2 == 0:  # Check if the number is even
        sum_even += n
    n += 1

print("Sum of even numbers from 1 to 10:", sum_even)