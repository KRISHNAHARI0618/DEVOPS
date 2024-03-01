"""
1: Create an Array and Traverse
2: Accessing Individual Array
3: Append any Value to the array
4: Insert element to an array
5: Extend Array From another array
6: Add Items from list to array using from list
7: Remove Element from an Array using remove method
8: remove last element from an array using pop()
9: remove element from array particular element
10: Reverse an array using python reverse method
11: get array buffer information through buffer_info()
13: Sort an array using sorted method
14: Check for number of occurrences of an element
15: Slicing Array
"""

from array import *

myArray = array('i',[12, 23, 34, 45, 56, 67, 78, 89, 90])
print(myArray)


for i in range(len(myArray)):
    print(myArray[i])

myArray.append(99)

print(myArray)
print(len(myArray))

myArray.insert(5,45)
print(myArray)

myArray2 = array('i',[10, 20, 30, 40, 50])
myArray.extend(myArray2)
print(myArray)

list1 = [35, 45, 55, 65, 75, 85]
myArray.fromlist(list1)
print(myArray)

myArray.reverse()
print(myArray)

myArray.buffer_info()
print(myArray)

sortArray = sorted(myArray)
print(sortArray)

print(myArray.count(45))

strArray = sortArray.__str__()
print(type(strArray))

print(sortArray[2:7])

