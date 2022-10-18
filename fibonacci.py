def fib(howManyNums):
    if(howManyNums<=0):
        print(f'{howManyNums} is not a positive number!')
    else:
        fibNums = [1]
        for i in range(howManyNums):
            fibNums.append(fibNums[i]+fibNums[i-1])
        print(fibNums)

fib(int(input('How many Fibonacci numbers: ')))
