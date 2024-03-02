import math
import numpy

# Using In build Function

result = math.factorial(5)
print(result)

# using recursive function

def fact(n):
  if n==0:
    return 1
    # break
  else:
    return n*fact(n-1)
result  = fact(6)
print(result)

def factorial(n):
  return 1 if (n == 1 or n == 0) else n*factorial(n-1)

print(factorial(5))

# Using Iterative approach

def factorial(n):
  if n<0:
    return 0
  elif ( n == 0 or n ==1 ):
    return 1
  else:
    fact = 1
    while n != 0:
      fact = fact*n
      n = n-1
    return fact
print(factorial(5))
print(factorial(0))
print(factorial(-2))

def factorial(n):
  res = 1
  for i in range(2,n+1): # 2,3,4,5
    res = res*i
  return res
print(factorial(6))
n = 5
x = numpy.prod([i for i in range(1,n+1)])
print(x)