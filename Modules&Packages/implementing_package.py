from math_library.arithmetic import product
from math_library.geometry import Rectangle, Triangle

num1 = 10
num2 = 20
multiplication = product(num1,num2)
print("Product of given numbers is {}".format(multiplication))

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

triangle = Triangle(3, 8)
print("Triangle Area:", triangle.area())
