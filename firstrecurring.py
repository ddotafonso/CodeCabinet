# Given an array return the first recurring function


# Time complexity of 0(n) and space complexity of O(n)
array1 = [2, 5, 3, 3, 3, 4, 6, 7]
array2 = [1, 3, 5, 5, 9, 4, 4, 1]

def recurringNumber(x):
    recurred = {}
    for value in x:
        if value in recurred:
            return value
        else:
            recurred[value] = 0
    return None
    

print(recurringNumber(array2))