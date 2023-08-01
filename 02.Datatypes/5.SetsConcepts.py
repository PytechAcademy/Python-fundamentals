## Creating a set
# Using curly brace notation
my_set = {1, 2, 3, 4, 5}
# Using the set() constructor
my_set = set([1, 2, 3, 4, 5])
## Basic Operations on Sets
# Adding Elements to a Set
my_set.add(6)
print("Adding 6 to the set:", my_set)
# Removing Elements from a Set
my_set.remove(3)
print("Removing 3 from the set:", my_set)
# Membership Testing
if 3 in my_set:
    print("3 is present in the set.")
else:
    print("3 is not present in the set.")
## Set Operations
print("4. Set Operations:")
setA = {1, 2, 3}
setB = {3, 4, 5}
# Union
union_set = setA.union(setB)
print("Union of setA and setB:", union_set)
# Intersection
intersection_set = setA.intersection(setB)
print("Intersection of setA and setB:", intersection_set)
# Difference
difference_set = setA.difference(setB)
print("Difference between setA and setB:", difference_set)
# Symmetric Difference
symmetric_diff_set = setA.symmetric_difference(setB)
print("Symmetric difference between setA and setB:", symmetric_diff_set, "\n")
## Use Cases for Sets
# Finding Unique Elements
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers)
print("Finding unique elements in a list:", unique_numbers)
# Eliminating Duplicates from Lists
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_names = list(set(names))
print("Eliminating duplicates from a list:", unique_names, "\n")
