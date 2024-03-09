from cgi import test
import random
from typing import Counter
'''
test_dict  = {
  'gfg':[10,20,30,40,50],
  'is':[20,30,40,80],
  'too':[50,60,80,90,27],
  'good':[60,20,27,87,67],
  'good':[60,20,27,87,67]
}
print(test_dict["gfg"])
print(test_dict['good'])
print(test_dict['is'])
print(test_dict['too'])
print(len(test_dict))

thisdict = dict(name="hari",section="abc",year=2024)
print(thisdict)

print(test_dict.items())

valueslist = []
for keys,values in test_dict.items():
  for value in values:
    valueslist.append(value)

print(list(set(valueslist)))
print(list(set(sum(test_dict.values(),[]))))
# print()
freq = Counter(valueslist)
uniqueValues = list(freq.keys())
uniqueValues.sort()
print(uniqueValues)

# for element in "ababababsjaksi":
#   print(element,end=" ")
'''
obj_list = ["a","b","c","d","e","f","g"]

counter = Counter()

dict = {} # declaration empty dictionary
for obj in obj_list:
  dict[obj] = 0 # initialization empty string

print(dict)
for _ in range(100):
  # print(random.choice(obj_list),end=" ")
  return_objects = random.choice(obj_list)
  # print(return_objects,end=" ")k
  dict[return_objects] = dict[return_objects] + 1
print(obj_list)

print(dict)

# for _ in range(100):
#   print(random.choice(obj_list),end=" ")
#   return_objects = random.choice(obj_list)
#   counter[return_objects] = counter[return_objects]+1
# print(counter)