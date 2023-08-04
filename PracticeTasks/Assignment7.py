# Find divisors in given range of numbers for a selected number
a = int(input('Enter the first num:'))
b = int(input('Enter the second num:'))
c = int(input('Enter the third num:'))
divisors = []
for i in range(a,b):
    if i%c == 0:
        divisors.append(i)
print(divisors)
print(len(divisors))
