# Create a Dictionary
import functools
import numpy as np


test_dict = {
  'gfg':100,
  'is' : 200,
  'good':300
}
print(sum(list(test_dict.values())))

# sum = 0
# for i in test_dict.values():
#   sum = sum + i
# print(sum)

def returnSum(dict):
  return sum(dict.values())

print(returnSum(test_dict))

# Using Numpy
def returnSum(dict):
  values = np.array(list(dict.values()))
  return np.sum(values)

print(returnSum(test_dict))

# using Functools

def returnSum(dict):
  return functools.reduce(lambda acc,x:acc+dict[x],dict,0)
print(returnSum(test_dict))

# using normal key method

def returnSum(dict):
  return sum(dict[key] for key in dict)

print(returnSum(test_dict))

for key in test_dict:
  print(test_dict[key])