"""
arr = [10,45,20,30,56,11,23]
max = arr[0]
n = len(arr)
for i in range(1,n):
  if arr[i] > max:
    max = arr[i]
print(max)
"""
from functools import reduce


def largest(arr,n):
  ans = max(arr)
  return ans

if __name__ == '__main__':
  arr = [10,34,56,36,89,15]
  n = len(arr)
  print("The maximum number from the array is: ", largest(arr, n))

# Sort Method

def sortMethod(arr,n1):
  arr.sort()
  return arr[n1-1]

if __name__ == '__main__':
  arr = [10,45,60,34,76,23,56,87,11,12,14,15,17]
  n1 = len(arr)
  ans = sortMethod(arr,n1)
  print("The largest Number in array is :", ans)

# Reduce Method

def reduceMethod(arr):
  ans = reduce(max,arr)
  return ans

arr = [20,40,60,45,90,11,14,15]
ans = reduceMethod(arr)
print("Largest Number is :", ans)

# Sum Method

def sumMethod(arr):
  ans = reduce(sum,arr)
  return ans
arr = [20,40,60,45,90,11,14,15]
ans = sumMethod(arr)
print("Largest Number is :", ans)





