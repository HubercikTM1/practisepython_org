word = (input('Write any word: ')).lower()
letters = []

for i in word:
    letters.append(i)

print(letters)

#[::-1] - reversing a string, list or any iterable with an ordering
if letters==letters[::-1]:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
