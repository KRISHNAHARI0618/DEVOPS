print(" Om Namo Vinayakaya Namahh  ")
print(" Om Namo Venkateshaya Namahh")

# Mathematical Problems:
#1: Sum of First N Natural Numers : n*(n+1)/2

#2: Counter

# def counter(n):
#   res = 0
#   while n != 0:
#     n = n//10
#     res = res + 1
#   return res
# print(counter(1234))

# Fibonacci Series:
# Palindrome:

# print(isPal(121))

# GCD Eucliedian Theorem

def Gcd(a,b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a

print(Gcd(12,15))

# count trailing 0s
# in n !
# Function to return # trailing 0s in # factorial of n def findTrailingZeros(n):
# # Initialize result
count = 0
# # Keep dividing n by
# # powers of 5 and
# # update
# Count i = 5
# while (n / i >= 1):
#   count += int(n / i) i *= 5
#   return int(count)
# Driver program n = 100 print("Count of trailing 0s "+ "in 100 ! is", findTrailingZeros(n))\

def findTrailingZeros(n):
  count = 0
  i = 5
  while (n/i > 1):
    count = count + int(n/i)
    i = i * 5
  return int(count)

print(findTrailingZeros(5))
