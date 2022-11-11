def reverseWords(sentence):
    splitSent = sentence.split(' ')
    splitSent.reverse()
    for i in range(len(splitSent)):
        print(splitSent[i])


sent = "first test sentence"
reverseWords(sent)
