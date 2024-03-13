test_dict = {
  'month' : [1,2,3,4,5],
  'name':['Jan','Feb','March','Apr']
}

print("Th Dictionary is : ", test_dict)

# Flatten Dictionary with zip and dict functions

flatten_dict = dict(zip(test_dict['month'],test_dict['name']))
print(flatten_dict)

# Zip Functions

names = ['Hari','akhila','Ramana','bharathi','harsha']
rollNos = [1,2,3,4,5]

zip_func = zip(names,rollNos)
print(dict(zip_func))

# Convert dictionary form lists in dictionaries

list_dict = {
  'names': ['andhra','telangana','tamilnadu','karnataka','kerala'],
  'state_no': [2,5,7,9,13]
}
print(list_dict)
print(dict(zip(list_dict['names'],list_dict['state_no'])))
print(set(zip(list_dict['names'],list_dict['state_no'])))
print(tuple(zip(list_dict['names'],list_dict['state_no'])))
print(list(zip(list_dict['names'],list_dict['state_no'])))






