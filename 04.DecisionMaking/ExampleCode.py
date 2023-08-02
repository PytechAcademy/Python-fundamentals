# single condition check
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
# Check for even or odd number
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# Grading conversion
percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
else:
    print("Grade: F")