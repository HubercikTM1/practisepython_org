def inList(numsList, num):
    if(num in numsList):
        print(f'{num} is in the list: {numsList}')
        return True
    else:
        print(f'{num} is not in the list: {numsList}')
        return False

nums = [3,4,5,6,7,8,9]
inList(nums,7)
