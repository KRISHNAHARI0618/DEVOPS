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


