print(" Om Namo Vinayakaya Namahh  ")
print(" Om Namo Venkateshaya Namahh")

# Mathematical Problems:
#1: Sum of First N Natural Numers : n*(n+1)/2

#2: Counter

def counter(n):
  res = 0
  while n != 0:
    n = n//10
    res = res + 1
  return res
print(counter(1234))

# Fibonacci Series:
# Palindrome:
def counter(n):
  res = 0
  temp = n
  while n != 0:
    # n = n%10
    res = res + 10*(n%10)
    n = n//10
  return res == temp
print(counter(121))