# Generate List of Squares of Even number and Cubes for odd numbers

return_list = [ x**2 if x%2 == 0 else x**3 for x in range(1,11) ]

print(return_list)


# Fibonacci
list_fib = []
n1 = 0
n2 = 1
for i in range(5):
  list_fib.append(n1)
  # n3 = n1+n2
  n1,n2  = n2,n1+n2
  n1 ,n2 = n2 , n1
  # n2 = n1+n2
  # list_fib.append(n1)
print(list_fib)
  # n3 = n1+n2
  # print(n3)
# n3 = n1+n2
# print(n3)
# n1 = n2
# n2 = n3
# n3 = n1+n2
# print(n3)

def generate_fibonacci(n):
  fib_sequence = []
  a,b = 0,1
  for _ in range(n):
    fib_sequence.append(a)
    a,b = b,a+b

  return fib_sequence

num_terms = 10
result = generate_fibonacci(num_terms)
print(result)

# Swapping Numbers
a = 10
b = 20
a,b = b,a
print(a,b)

# Word Count
'''
algorithim
'''