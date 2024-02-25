import array

array1 = array.array('i',[2, 3, 4, 5, 6, 7, 8])


def accessElement(array2, index):
    if index >= len(array2):
        print("The element is not present in the list ")
    else:
        print(array2[index])


accessElement(array1,2)

