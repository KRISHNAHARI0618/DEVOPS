# # Eucledian Algorithim
# def Gcd(a,b):
#   while a != b:
#     if a > b :
#       a = a - b
#     else:
#       b = b - a
#   return a
# print(Gcd(12,15))

# Using optimized Eucliedian Algorithim
# from symbol import func_body_suite


print("This is another way to success")

def gcd(a,b):
  if b == 0:
    return a
  return gcd(b, a % b)

12,15
15,12
12,3
3,0

print(gcd(12,15))

'''
hcf(a,b)

hcf(12,15) --> hcf(15,12%15)

hcf(15,12) --> hcf(12,15%12)

hcf(12,3) --> hcf(3,12%3)

hcf(3,0) --> if b == 0 return a = 3

hcf(12,3) -->


'''
def return_stst(b):
  if b == 0:
    return 5
print(return_stst(0))


# Getting the divisors

def divisors(a):
  for i in range(1,a+1):
    if a % i == 0:
      print(i)

divisors(10)

count = 1
while count <=5:
  print(count)
  count = count+1
# print()


print("GCD of two numbers")

def gcd2(a,b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  print(a)

gcd2(10,20)
gcd2(20,89)
gcd2(12,15)
gcd2(2,1)


def fun_gcd(a,b):
  if b == 0:
    return a
  else:
    return fun_gcd(b,a%b)
print(fun_gcd(10,20))



