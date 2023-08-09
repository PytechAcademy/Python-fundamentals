# using module and its name directly
import math_operations
num1 = 10
num2 = 80
sum = math_operations.add(num1,num2)
difference = math_operations.subtract(num1,num2)
print("Sum of given numbers is {} and Difference is {}".format(sum,difference))

# using module and alias name
import math_operations as mo
num1 = 10
num2 = 80
sum = mo.add(num1,num2)
difference = mo.subtract(num1,num2)
print("Sum of given numbers is {} and Difference is {}".format(sum,difference))
