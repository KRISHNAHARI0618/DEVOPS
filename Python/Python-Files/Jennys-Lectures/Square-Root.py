# Armstrong Number Number of n digits which are equal to sum of nth power of its digits

number = 123
leng = len(str(number))
print(len(str(number)))

for i in range(0,leng):
  print(number)

for i in range(1001):
  number = i
  result = 0
  n = len(str(i))
  while(i != 0 ):
    digit  = i%10
    result = result+digit**n
    i = i//10
  if number == result:
    print(number)
# print(result,end=" ")
