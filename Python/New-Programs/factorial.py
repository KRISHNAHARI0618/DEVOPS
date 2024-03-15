# def fact(n):
#   if n == 0:
#     return 1
#   else:
#     return n * fact(n-1)

# print(fact(10))

def fact(n):
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  else:
    fact1 = 1
    while n > 1:
      fact1 = fact1 * n
      n = n -1
    return fact1

print(fact(5))

# Trailing Zeros Factorial