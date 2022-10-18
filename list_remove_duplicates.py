def delDuplicates(l):
    noDup = []
    for i in l:
        if(i not in noDup):
            noDup.append(i)
    print(noDup)


def setDuplicates(x):
    print(list(set(x)))

a = [3,5,6,2,3,7,8,9,1,5]
print(a)
delDuplicates(a)
setDuplicates(a)
