
# The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object
# Syntax: enumerate(iterable, start=0)
# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
# Return: Returns an iterator with index and element pairs from the original iterable

import enum


list1 = ['hari','vardhan','reddy']
list2 = list(enumerate(list1))
print(dict(list2))

name = 'peddireddy'
print(list(enumerate(name,5)))

for ele in enumerate(name):
  print(ele)

for ele,count in enumerate(name,100):
  print(ele,count)

enum_names = enumerate(name)
next_name = next(enum_names)
for i in next_name:
  print(i)
print(next_name)
