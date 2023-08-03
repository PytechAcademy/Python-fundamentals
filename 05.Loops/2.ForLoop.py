# Iterating through string
String = 'Hello world'
for i in String:
    print(i)
# Iterating through List
List = [1, 2, 3, 'John']
for i in List:
    print(type(i))
# Iteration using range concept in a list
List = [1, 2, 3, 'John']
for i in range(len(List)):  # Equivalent to for i in range(4)
    print(List[i])