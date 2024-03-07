import numpy
import array

array1 = [10, 20, 30, 40, 50, 60]
array2 = [[10, 20], [30, 40], [50, 60]]

print("\b", array2, "\n")

for i in range(len(array2)):
    for j in range(len(array2) - 1):
        print(array2[i][j], id(array2[i][j]))

print(" \n  ********* \n  ")

def printArray():
    for i in range(len(array1)):
        array_id = id(array1[i])
        print(i, array_id)

printArray()


