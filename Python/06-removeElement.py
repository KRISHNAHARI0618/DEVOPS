import array

removeArray = array.array('i',[23, 34, 45, 67, 78, 89, 100])

print(removeArray)

addingElements = []


def removeElement(array, target):
    for i in range(len(array)):
        if i == target:
            continue
        else:
            addingElements.append(array[i])


removeElement(removeArray,4)

print(addingElements)