number = 32

print(number)
flag = False
for i in range(2,number):
  if number % i == 0:
    flag = True
    break

if flag:
  print(number,"this is not a prime number")
else:
  print(number,"this is prime number")
"""
lower = int(input("Enter Lower Number: "))
upper = int(input("Enter my number: "))
for num in range(lower,upper+1):
  if num>1:
    for i in range(2,num):
      if num%i == 0:
        break
    else:
      print(num,end=",")
print()
"""
start = int(input("Please enter where to start numbers: "))
end = int(input("Please enter where to end the loop : "))
for num in range(start,end+1):
  if num>1:
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      print(num,end=" ")

  # print(num,end=" ")
# Add PrimeNumbers to List
print("\n")
primeNumbers = []

start = int(input("Where to start: "))
end = int(input("Where to End: "))

for num in range(start,end):
  if num>1:
    for i in range(2,num):
      if num % i == 0:
        break
    else:
      primeNumbers.append(num)
print(primeNumbers)
# print("\n")
sum = 0
for i in primeNumbers:
  sum = sum + i
print(sum)

# print("\n")

