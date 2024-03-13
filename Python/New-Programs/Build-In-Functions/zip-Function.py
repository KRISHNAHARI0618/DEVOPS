# ZIP Method : Takes a multiple iterable objects and give sthe single iterable object having with mapped values form all containers

# Syntax :  zip(*iterators)
# Parameters : Python iterables or containers ( list, string etc )
# Return Value : Returns a single iterator object.\
# Zip Function will do the mapping of all the elements in each iterator


# from networkx import enumerate_all_cliques


list1 = [1,2,3,4,5,6]
list2 = [9,8,7,6,5,4]

list3 = zip(list1,list2)
print(list3)

for i in list3:
  print(i)

name1 = 'Hari'
name2 = 'vardhan'
name3 = zip(name1,name2)
print(set(name3))
for i in name3:
  print(i)
# name

# Zip Function with enumerate function
# Enumerate method will iterate over multiple objects or containers at a time only 2

list1 = [1,2,3,4,5]
list2 = [0,9,8,7,6]
list3 = [7,6,5,4,3]

obj1 = enumerate(list1)
print(list(enumerate(list1)))

# for i,j in enumerate(tuple(list1),tuple(list2)):
#   print(i,j)


names = ['hari','akhila','reddy','vardhan','peddireddy']
ages = ['24','22','21','67','54']

for i, (name,age) in enumerate(set(zip(names,ages))):
  print(i,name,age)

# zip function with dictionary

stocks = ['hdfc','for','geeks']
prices = [2571,1127,2750]

new_dict = {stock:price for stock,price in zip(stocks,prices) }

print(new_dict)

# zip function for convert them into list
tuple1 = (1,2,3)
tuple2 = ('accenture','infosys','wipro')
mapped = zip(tuple1,tuple2)
lsit = list(mapped)
print(lsit)
