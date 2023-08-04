# Check num is prime or not
num = int(input('Enter the number: '))
remainders = []
divisors = []
for i in range(1,num+1):
    remainder = num%i
    if remainder == 0:
        remainders.append(remainder)
        divisors.append(i)
print(divisors)
if len(remainders)==2:
    print('Given num is prime')
else:
    print('Num is not prime')

