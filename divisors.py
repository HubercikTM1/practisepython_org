#divisor - dzielnik
num = int(input('Write a number: '))
divisors = []

for i in range(num):
    if(num%(i+1)==0):
        divisors.append(i+1)
    else:
        print(f'{i+1} is not a divisor of {num}')

print(f'divisors of {num} are: {divisors}')
