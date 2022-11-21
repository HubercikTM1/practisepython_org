import random

def cows_bulls():
    randNum = random.randint(1000,9999)
    cowsBulls = []
    numOfGuesses = 0
    print('Welcome to the Cows and Bulls Game!')

    while True:
        print((randNum))

        guessesNum = input('Guess a number:\n')
        numLen = len(guessesNum)
        if(numLen!=4):
            print('This is not a 4-digit number!')
            continue
        elif(numLen==4 and int(guessesNum)!=randNum):
            #in the correct place - cow
            #in the wrong place - bull
            r_num = [int(x) for x in str(randNum)]
            g_num = [int(y) for y in str(guessesNum)]

            #print(f'randNum: {r_num}')
            print(f'guessedNum: {g_num}')

            for i in range(len(g_num)):
                if(g_num[i]==r_num[i]):
                    cowsBulls.append('cow')
                elif(g_num[i] in r_num and g_num[i]!=r_num[i]):
                    cowsBulls.append('bull')

            numOfGuesses+=1
            print(f'{cowsBulls.count("cow")} cows, {cowsBulls.count("bull")} bulls')
            cowsBulls.clear()
            continue

        elif(int(guessesNum)==randNum):
            print(f'Correct! The number was {randNum}')
            print(f'You tried to guess the number {numOfGuesses} times!')
            False
            break


if __name__ == '__main__':
    cows_bulls()
