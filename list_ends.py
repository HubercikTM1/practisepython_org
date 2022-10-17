def listEnds(numbers):
    firstLast = []
    listLen = len(numbers)
    firstLast.append(numbers[0])
    firstLast.append(numbers[listLen-1])
    print(firstLast)

numbers = [10, 25, 37, 52, 60]

listEnds(numbers)
