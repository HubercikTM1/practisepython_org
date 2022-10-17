def primeCheck(num):
    divisors = []
    numDivisors = []

    if(num<0):
        print('A negative number is not a prime number!')
    elif(num==0):
        print(f'{num} is not a prime number!')
    
    else:
        for i in range(num):
            divisors.append(i + 1)

        for j in range(len(divisors)):
            if (num % divisors[j] == 0):
                numDivisors.append(divisors[j])
        print(f'divisors of {num} are {numDivisors}')

        if (len(numDivisors) <= 2):
            print(f'{num} is a prime number')
        else:
            print(f'{num} is not a prime number')


primeCheck(int(input('Check if this number is prime: ')))
