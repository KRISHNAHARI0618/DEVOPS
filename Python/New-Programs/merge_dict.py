# Python code to merge dict using update() method
def Merge(dict1, dict2):
	return(dict2.update(dict1))


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This returns None
# print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)

def Merge(dict1, dict2):
  return(dict2.update(dict1))

dict1 = {'abc': 'hari','def': 'harsha'}
dict2 = {'ghi': 'bharathi', 'jkl': 'ramana'}

# print(Merge(dict1,dict2))
print(dict2)