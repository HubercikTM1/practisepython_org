import random
import string

while True:
    boolPass = input("Do you want to generate a password?\nY - yes\nN -no\n")
    if(boolPass=='Y'):
        howStrong = input("How strong password do you want?\n1 - weak\n2 - medium\n3 - hard\n")
        if (howStrong == '1'):
            passWeak = ""
            for i in range(random.randint(2,10)):
                randomWeak = ''.join([random.choice(string.ascii_letters)])
                passWeak+=randomWeak
            print(passWeak)
            break

        elif (howStrong == '2'):
            passMedium = ""
            for i in range(random.randint(5, 14)):
                randomMedium = ''.join([random.choice(string.ascii_letters + string.digits)])
                passMedium += randomMedium
            print(passMedium)
            break

        elif (howStrong == '3'):
            passHard = ""
            for i in range(random.randint(8, 20)):
                randomHard = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation)])
                passHard += randomHard
            print(passHard)
            break

        else:
            print("Wrong input!")
            continue

    elif(boolPass=='N'):
        print('OK, Thank you')
        break
    else:
        print('Wrong input!')
        continue
