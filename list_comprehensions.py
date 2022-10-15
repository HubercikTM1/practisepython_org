a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#even - parzysty
even = []
for num in a:
    if num%2==0:
        even.append(num)
    else:
        print(f'{num} is odd')

print(f'List of even numbers: {even}')
