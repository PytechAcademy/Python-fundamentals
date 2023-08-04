# Finding greatest of three numbers
a = float(input('Enter the first num:'))
b = float(input('Enter the second num:'))
c = float(input('Enter the third num:'))
if a>b and a>c:
    print('a is greater')
elif b>a and b>c:
    print('b is greater')
elif c>a and c>b:
    print('c is greater')
else:
    print('num might be equal')

