# Terminating a sequence
for i in range(1, 11):
    if i == 5:
        break  # The loop will terminate when i becomes 5
    print(i)

# Searching for element in a sequence
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
search_item = 'orange'

for fruit in fruits:
    if fruit == search_item:
        print(f'{search_item} found in the list!')
        break
else:
    print(f'{search_item} not found in the list.')

