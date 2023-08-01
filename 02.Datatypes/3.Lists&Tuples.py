### List operations
## Creating a List
A = ['John', 14, 9.0]
## Length of list
print(len(A))   # Output: 3
## Indexing and slicing
print(A[0])     # Output: 'John'
print(A[1:])    # Output: [14, 9.0]
## Adding elements to list
# adding one element at a time
A.append('Mary')
print(A)        # Output: ['John', 14, 9.0, 'Mary']
A.append(99)
print(A)        # Output: ['John', 14, 9.0, 'Mary', 99]
# adding sequence at once
B = (1, 2, 3, True, False)
A.extend(B)
print(A)        # Output: ['John', 14, 9.0, 'Mary', 99, 1, 2, 3, True, False]
## Updating elements
# If you know the index
A[0] = "Tom"
print(A)        # Output: ['Tom', 14, 9.0, 'Mary', 99, 1, 2, 3, True, False, (1, 2, 3, True, False)]
# If you do not know the index
Index_Mary = A.index('Mary')
A[Index_Mary] = "Tary"
print(A)        # Output: ['Tom', 14, 9.0, 'Tary', 99, 1, 2, 3, True, False, (1, 2, 3, True, False)]
## Inserting elements
A.insert(1, 'Leila')
print(A)        # Output: ['Tom', 'Leila', 14, 9.0, 'Tary', 99, 1, 2, 3, True, False, (1, 2, 3, True, False)]
## Removing elements
# deleting one at once
A.pop(1)
print(A)        # Output: ['Tom', 14, 9.0, 'Tary', 99, 1, 2, 3, True, False, (1, 2, 3, True, False)]
# deleting range of elements
del A[1:3]
print(A)        # Output: ['Tom', 'Tary', 99, 1, 2, 3, True, False, (1, 2, 3, True, False)]
# deleting by value
A.remove(True)
print(A)        # Output: ['Tom', 'Tary', 99, 1, 2, 3, False, (1, 2, 3, True, False)]
## Clearing the list
A.clear()
print(A)        # Output: []
## Reverse
B = [3, 2, 1]
B.reverse()
print(B)        # Output: [1, 2, 3]
## Sort
C = [5, 1, 4, 2, 3]
C.sort()
print(C)        # Output: [1, 2, 3, 4, 5]
## Copy
D = C.copy()
print(D)        # Output: [1, 2, 3, 4, 5]
E = C[:]
print(E)        # Output: [1, 2, 3, 4, 5]
## Count of elements
numbers = [1, 2, 3, 2, 4, 2, 5]
print(numbers.count(2))  # Output: 3
## Membership test
fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)   # Output: True
print('grape' in fruits)    # Output: False
## List comphrension
# Example: Create a new list with squares of elements from the original list
original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]
print(squared_list)        # Output: [1, 4, 9, 16, 25]
## max and min from a list
numbers = [10, 5, 20, 15]
print(max(numbers))     # Output: 20
print(min(numbers))     # Output: 5
## sum of elements in list
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))     # Output: 15
## sorting of list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)   # Output: [1, 1, 2, 3, 4, 5, 6, 9]
# enumerate
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: orange
### Work on tuples with same operations above and understand the concept

### List and Tuple conversion
list_example = [1, 2, 3]
tuple_example = tuple(list_example)
print(tuple_example)    # Output: (1, 2, 3)
tuple_example = (4, 5, 6)
list_example = list(tuple_example)
print(list_example)     # Output: [4, 5, 6]
