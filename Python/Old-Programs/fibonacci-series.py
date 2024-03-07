lower = int(input("enter number of fibonacci series : "))

n1 = 0
n2 = 1
for i in range(lower):
  print(n1)
  n3 = n1
  n1 = n2
  n2 = n2+n3

number = int(input("Enter Another Set of Numbers: "))
firs_number = 2
second_number = 8
print(firs_number)
print(second_number)
for i in range(2,number):
  third_number = 2*second_number -firs_number
  firs_number = second_number
  second_number = third_number
  print(third_number)
  # temp = firs_number
  # first_number = second_number
  # second_number = 2*second_number - first_number