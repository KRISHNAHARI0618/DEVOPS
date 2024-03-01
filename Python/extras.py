for i in range(100):
  if i>1:
    for j in range(2,i):
      if i%j == 0:
        break
    else:
      print(i)

# sum of the remainders

number = 153
str_num = str(number)
len_num = len(str_num)

for i in range(len_num):
  print(i)