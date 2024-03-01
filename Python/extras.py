# Prime Numbers

from numpy import power


for i in range(100):
  if i>1:
    for j in range(2,i):
      if i%j == 0:
        break
    else:
      print(i,end=" ")

print()
# Armstrong Numbers

number = 153
str_num = str(number)
len_num = len(str_num)
sum = 0

for i in str_num:
  sum = sum + int(i)**len_num
print(sum)

# Another way of printing the armstrong number

x = 4
y = 7
print(x//y) # Quotient
print(x%y) # Remainder
print(x/y) # Floating Quotient

print(power(6,y//2)) # power(x,y//2)*
print(power(x,y//2)) #* power(6,y//2)


