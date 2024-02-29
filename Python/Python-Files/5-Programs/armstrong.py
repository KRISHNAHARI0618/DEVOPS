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
