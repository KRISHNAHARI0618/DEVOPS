# Introduction to Python Course
'''
Python is a Programming language
Fastest Growing Language
Machine Learning
Hacking
Artificial Intelligence
History Of Language:

1: Simple Structured
'''
import os
from tarfile import LENGTH_PREFIX


print("Hello World")
print("Hello World",end=" ")
print("Hello World",end=" ")

for i in range(10):
  for j in range(i):
    print(i,j, end=" ")

# Matrix Problem
# Syntax Errors

os.rename()
print()
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[9,8,7],[6,5,4],[3,2,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
  for j in range(len(X[0])):
    result[i][j] = X[i][j] + Y[i][j]

for r in result:
  print(r)