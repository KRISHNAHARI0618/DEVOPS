from typing import OrderedDict

# adding dictionary at the begging using ordered dict

dict = {'hari':2000,'age':24}
new_dict = {'course':'DevOps2024'}

initOrderedDict = OrderedDict(dict)

initOrderedDict.update(new_dict)
initOrderedDict.move_to_end('course',last=False)

print(str(initOrderedDict))

# Using Naive Method

dict1 = {'hari':2000,'age': 24}
dict2 = {'year':2024,'yardly':356}
list1 = list(dict1.items())
list2 = list(dict2.items())
con_list = list2+list1
# print(dict(con_list))
print(con_list)


dict1 = {'apple':1,'banana':2,'cat':3,'dog':4,'elephant':5}
print(dict1)
dict2 = {'fat':6,'goat':7}
order_dict1 = OrderedDict(dict1)
order_dict2 = order_dict1.update(dict2)
order_dict1.move_to_end('fat',last=False)

print(order_dict1)

