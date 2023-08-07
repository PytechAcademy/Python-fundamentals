def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase
    s = s.replace(" ", "")  # Remove spaces from the string
    return s == s[::-1]  # Check if the string is equal to its reverse

# Taking input from the user
input_string = input("Enter a string: ")

# Checking if the string is a palindrome
result = is_palindrome(input_string)

# Displaying the result
if result:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
