def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

# Taking input from the user
input_numbers = input("Enter a list of integers separated by spaces: ")
numbers_list = [int(num) for num in input_numbers.split()]

# Calculating sums of even and odd numbers
even_sum, odd_sum = sum_even_odd(numbers_list)

# Displaying the results
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
