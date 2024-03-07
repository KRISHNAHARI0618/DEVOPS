a = int(input("Enter a Value: "))
b = int(input("Enter b Value: "))

# a,b = 2,4
print(a+b)
print(max(a,b))

# Ternary Operator
print(a if a>b else b)

# Using Lambda Function
maximum_number = lambda a,b : a if a>b else b
print(f"{maximum_number(a,b)} is a maximum Number")

# using List Comprehension

c = []
for i in range(5):
  a = int(input("Enter a Value: "))
  b = int(input("Enter b Value: "))
  x = [a if a>b else b]
  c.append(x)
print(c)

# Sort Method

c.sort()
print(c[-1])

# Using Maximum Function

def maximum(a,b):
  if a>b:
    print(a)
  else:
    print(b)
maximum(10,20)