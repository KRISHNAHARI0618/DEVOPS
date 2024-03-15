def isPal(n):
  rev = 0
  temp = n
  while temp != 0:
    rem = temp % 10  #
    rev = rev * 10 + rem
    temp = temp // 10
  return rev == n
print(isPal(121))

for i in range(11,1001):
  if isPal(i):
    print(i)

