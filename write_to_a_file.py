fileName = input('What name of the txt file od you want?\n')
fileOutput = input('What text do you want in the file?\n')

with open(f'{fileName}.txt', 'w') as f:
    f.write(f'{fileOutput}')
