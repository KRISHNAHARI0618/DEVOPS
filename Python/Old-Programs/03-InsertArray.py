import numpy as np
import array

variable = 42
memory_address = id(variable)
print(f"The memory Address of the variable is : {memory_address}")

myArray = array.array('i', [1, 3, 4, 6, 8, 10])
print(myArray)

myArray.insert(2, 12)
print(myArray)

"""
Traversal Operation : Visiting all Sets of Elements with in an array

"""