import random

a = []
b = []
#common - wspolny
common_nums = []
a_len = random.randint(1,15)
b_len = random.randint(1,15)

print(f'len of a is {a_len}\nlen of b is {b_len}')

for i in range(a_len):
    a.append(random.randint(1,20))

for j in range(b_len):
    b.append(random.randint(1,20))

print(f'{a}\n{b}')

for k in range(a_len):
    for l in range(b_len):
        if(a[k]==b[l] and a[k] not in common_nums):
            common_nums.append(a[k])

print(f'common numbers are: {common_nums}')

