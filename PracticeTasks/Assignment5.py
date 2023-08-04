# Multiplication table
num = float(input('Enter the number: '))
for i in range(1, 11):
    def display(num):
        value = num * i
        return str(num) + ' x '+ str(i) + ' = '+str(value)
    print(display(num))