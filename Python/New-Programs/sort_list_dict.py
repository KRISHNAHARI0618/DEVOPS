# Initializing List of Dictionaries
from operator import itemgetter


list = [
  {'name':'peddireddy','age':24},
  {'name':'harivardhan','age':12},
  {'name':'reddy','age':35}
]

print(list[1])

print("List sorted by age using itemgetter method")

print(sorted(list,key=itemgetter('name')))
print("\r")

print(sorted(list,key=itemgetter('age','name'),reverse=True))

# Item getter will work only for list of dictionaries

# list = [10,25,12,22,36,21]
car = [
  {'name':'benx','year':2024,'model':'ben234'},
  {'name':'audi','year':2022,'model':'audi456'},
  {'name':'kia','year':2021,'model':'kia567'},
  {'name':'innova','year':2025,'model':'inno789'}
]
print(sorted(car,key=itemgetter('name','model')))

print(" \n \n \n \n")
# Using Lambda Function to sort the list of dictionaries
print(sorted(car,key=lambda item : item['year']))