# numeric - int, float, complex
a = 10
print(type(a))  # output is int
b = 4.678146
print(type(b))
c = 8 + 5j
print(type(c))
# string - can be declared using single quotes, double quotes or triple quotes
x = 'hello, this is "raja"'
y = """hello
this is raja"""
print(type(x), type(y))
# List - ordered collection of data, mutable
List = [1, 2, 3, 4.5, 7.98, 'raja', 'good']
print(List)
print(type(List))
# Tuple - ordered collection of data, immutable
Tuple = (1, 2, 3, 4.5, 7.98, 'raja', 'good')
print(type(Tuple))
# Set - contains unique data without duplicates
Set = {1, 1, 2, 3, 4, 5, 6, 6, 6, 8, 9}
print(Set)
Area_data = ['Tim', 'Tom', 'Mary', 'Tim', 'Mary', 'Alex']
Set_unique_names = set(Area_data)
print(Set_unique_names)
# Dictionary - data stored in key value pairs
Dictionary = {'Alejandra': 10, 'Gulcin': 12, 'Jelena': 11}
print(type(Dictionary))
print(Dictionary['Gulcin'])
# boolean datatypes - True, False
print(10 > 11)
print(11 < 15)
