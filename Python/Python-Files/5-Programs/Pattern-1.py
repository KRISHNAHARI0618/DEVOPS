# Print Patterns

def pattern(n):
  for i in range(0,n):
    print(i,end=" ")

pattern(5)
print()

def pattern(n):
  for i in range(n):
    for j in range(n):
      print(i,end=" ")
    print()
pattern(5)

def pattern(n):
  for i in range(n):
    for j in range(i+1):
      print(i,end=" ")
    print()
pattern(5)

def pattern(n):
  for i in range(n):
    for j in range(i+1):
      print(i,end=" ")
    print()
pattern(5)

def pattern(n):
  for i in range(n):
    for j in range(i,n):
      print(i,end=" ")
    print()
pattern(5)

def pattern(n):
  for i in range(n):
    for j in range(n-i):
      print(i,end=" ")
    print()
pattern(5)

def pattern(n):
  for i in range(0,n,1):
    for j in range(i,n,1):
      print(" ",end=" ")
    for j in range(0,i+1,1):
      print(i,end=" ")
    print()
pattern(5)

def pattern(n):
  for i in range(0,n,1):
    for j in range(0,i+1,1):
      print(" ",end=" ")
    for j in range(i,n,1):
      print(i,end=" ")
    print()
pattern(5)


# for i in range(start,stop,increment)