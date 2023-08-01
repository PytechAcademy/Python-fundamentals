# Creating a dictionary using curly brace notation
Dict = {'sape': 4139, 'guido': 4127, 'jack': 4098}
# Creating a dictionary using the dict() constructor
Dict_2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
## Operations on dictionaries
# Accessing elements in the dictionary
print(Dict['jack'])  # Output: 4098
# Getting the number of key-value pairs in the dictionary
print(len(Dict))  # Output: 3
# Getting a list of all keys in the dictionary
print(Dict.keys())  # Output: dict_keys(['sape', 'guido', 'jack'])
# Getting a list of all values in the dictionary
print(Dict.values())  # Output: dict_values([4139, 4127, 4098])
# Checking if a key exists in the dictionary
if 'sape' in Dict:
    print("Key 'sape' exists in the dictionary.")
# Adding a new key-value pair to the dictionary
Dict['sara'] = 3078
print(Dict)  # Output: {'sape': 4139, 'guido': 4127, 'jack': 4098, 'sara': 3078}
# Removing a key-value pair from the dictionary
del Dict['sara']
print(Dict)  # Output: {'sape': 4139, 'guido': 4127, 'jack': 4098}