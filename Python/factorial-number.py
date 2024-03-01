import math

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

