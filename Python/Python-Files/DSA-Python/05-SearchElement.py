"""
Linear Search Element
"""
import array

searchArray = array.array('i',[34, 56, 78, 98, 46, 36, 89])
print(searchArray)


def searchingElement(arrayName, targetSearch):
    for i in range(len(arrayName)):
        if arrayName[i] == targetSearch:
            return i
    return -1


x = searchingElement(searchArray,89)
print(x)



