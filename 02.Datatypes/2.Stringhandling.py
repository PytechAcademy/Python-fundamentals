# Length of a String:
String = 'Hello, World'
print(len(String))  # Output: 12

# Indexing:
print(String[4])  # Output: o
print(String[-3])  # Output: r

# Slicing:
print(String[3:])  # Output: lo, World

# Replacing Substrings:
String_modified = String.replace('e', 'a')
print(String_modified)  # Output: Hallo, World

# Converting String Cases:
print(String.upper())  # Output: HELLO, WORLD
print(String.lower())  # Output: hello, world
print(String.capitalize())  # Output: Hello, world

# Splitting a String:
Names = "A,G,J,M"
List_names = Names.split(',')
print(List_names)  # Output: ['A', 'G', 'J', 'M']

print(String.split())  # Output: ['Hello,', 'World']

# String Concatenation:
a = 'hello'
b = 'world'
print(a + b)  # Output: helloworld

# Membership Test:
print('c' in String)  # Output: False

# Membership Test with Conditional Statement:
if 'c' in String:
    print('c is part of the string')
else:
    print('C is not part of the string')  # Output: C is not part of the string

# String Stripping:
String_with_spaces = "   Hello, World   "
print(String_with_spaces.strip())  # Output: 'Hello, World'

# String Formatting (f-strings):
name = "John"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: 'My name is John and I am 30 years old.'

# String Joining:
words = ["Hello", "World", "Python"]
delimiter = " "
joined_string = delimiter.join(words)
print(joined_string)  # Output: 'Hello World Python'

# String Padding:
text = "Python"
left_padded = text.ljust(10, '-')  # Output: 'Python----'
right_padded = text.rjust(10, '=')  # Output: '====Python'

# String Checking (isX methods):
print('Hello'.isalpha())  # Output: True
print('123'.isdigit())  # Output: True
print('Hello123'.isalnum())  # Output: True
print('   '.isspace())  # Output: True
print('hello'.islower())  # Output: True
print('WORLD'.isupper())  # Output: True

# String Formatting (format() method):
name = "Alice"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: 'My name is Alice and I am 25 years old.'