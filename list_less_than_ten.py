a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessthanfive = []

for i in range(len(a)):
    if(a[i]<5):
        lessthanfive.append(a[i])
    else:
        print(f'{a[i]} is equal or greater than 5')

print(lessthanfive)
