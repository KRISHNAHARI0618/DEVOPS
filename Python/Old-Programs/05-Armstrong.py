# from symbol import power
"""

print(153/10)
print(153//10)
print(153%10)

number  = 153
sum = 0
b = len(str(number))
rev = number

while number != 0:
    remainder = number%10
    sum = sum + remainder ** b
    number = number//10
print(sum)
print(rev)
if rev == sum:
    print("The Given Number is Armstromg")
else:
    print("The given Number is not Armstrong")


def armstrongNumber(number):
    sum = 0
    arms = number
    b = len(str(number))
    while number != 0:
        remainder = number % 10
        sum = sum + remainder**b
        number = number//10
    if arms == sum:
        print("{} : is Armstromg Number" .format(arms))
    else:
        print("{} : is NOT Armstromg Number" .format(arms))

armstrongNumber(153)
armstrongNumber(255)
"""
# Algorithim Armstrong Number is sum of Cube of each number
# give the number
# Copy That number as another variable to compare
# initialize the Sum of number
# Traverse Through that number until number become zero
# take the remainder first
# Add initialized sum + remainder raised power of length of number
# then divide the number with 10 to get rid of last digit
# Compare both copied number and Sumed Number to get the result

from operator import iadd


print(5//2)

def power(x,y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power(x,y//2)*power(x, y//2)

    return x*power(x,y//2)*power(x,y//2)

print(power(2,0))

def order(x):
    n = 0
    while x != 0: # it will check the condition that x should not be equal to 0
        n = n+1
        x = x//10
    return n

print(order(11))

print(10/2) # This will give the Quotient with float symbol
print(10//2) # This will give the Quotient with integer symbol
print(10%2) #This will give remainder

def armstrong(x):
    n = order(x)
    temp = x
    sum = 0
    while temp != 0:
        r = temp % 10
        sum = sum + power(r,n)
        temp = temp // 10
    # return sum
    if x == sum:
        print("This is armstrong number")
    else:
        print("this is not an armstrong number")
    return sum

print(armstrong(153))

number = 153
str_num = str(number)
len_num = len(str_num)
sum = 0

for i in str_num:
    sum = sum + int(i)**len_num
print(sum)
    # print(i,type(i))

number = int(input("Enter the number: "))
str_num = str(number)
n = len(str_num)
sum = 0
for i in str_num:
  sum += int(i)**n
if sum == number:
  print(True)
else:
  print(False)

def arms(number):
  str_number = str(number)
  n = len(str_number)
  sum = 0
  for i in str_number:
    sum = sum + int(i)**n
  if sum == number:
    print(True)
  else:
    print(False)

arms(number)


# def armstrongNumber(number):
#   return sum(int(digit)**len(str(number)) for digit in str(number)) == number

# number = 153
# if armstrongNumber(number):
#   print(f"{number} is a Armstrong number")
# else:
#   print(f"{number} is not a armstrong number")





