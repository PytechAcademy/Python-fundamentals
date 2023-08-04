# Area of circle calculation by taking pi value from dictionary
Math = {'Pi':3.14,'e':2.71,'g':9.8}
## Area of circle
radius = float(input('Radius: '))
A = Math['Pi']*radius*radius
rounded_A = round(A,3)
print('Area of circle is {}'.format(rounded_A))