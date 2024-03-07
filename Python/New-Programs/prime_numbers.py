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