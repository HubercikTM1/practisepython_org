import random

num = random.randint(1,9)
guesses = 0

while True:
    userNum = input('Guess the number or type `exit` to quit: ')
    if(userNum=='exit'):
        print('You quitted the game!')
        break
    elif(int(userNum)>num):
        print('too high')
        guesses+=1
        continue
    elif(int(userNum)<num):
        print('too low')
        guesses+=1
        continue
    elif(int(userNum) == num):
        print('exactly right')
        guesses += 1
        break

print(f'It took you {guesses} guesses')
