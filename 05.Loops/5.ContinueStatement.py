# Skipping even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Removing duplicates in sequence
numbers = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 9]
unique_numbers = []
for num in numbers:
    if num in unique_numbers:
        continue
    unique_numbers.append(num)
print("List without duplicates:", unique_numbers)