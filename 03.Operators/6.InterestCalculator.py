# Get user input for principal amount, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a percentage): "))
time = float(input("Enter the time duration (in years): "))
# Calculate simple interest
interest = (principal * rate * time) / 100
# Display the result
print("Simple Interest:", interest)