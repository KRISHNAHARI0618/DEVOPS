'''
clear
'''

car = {
  'name' : "mahindraxuv500",
  'year' : 2024,
  'modelNo' : '2zv4'
}
print(car)
car.clear()
print(car)

class car:
  def __init__(self,name,year,modelNo):
    self.carName = name
    self.carYear = year
    self.carmodelNo = modelNo
    print(name,modelNo,year)

car1 = car('mahindra',2024,'xuv314')

car = {
  'name' : "mahindraxuv500",
  'year' : 2024,
  'modelNo' : '2zv4'
}

print(car)
x = car.copy()
print(x)

x = ('key1','key2','key3')
y = 0

dicti = dict.fromkeys(x,y)
print(dicti)

dicti = dict.fromkeys(x)
print(dicti)

print(dicti.get('key1'))
print(dicti['key1'])

x = dicti.items()
print(x)

x = dicti.keys()
y = dicti.values()
print(x,y)

list1 = [20,30,40]
list2 = ['a','b','c']
dictionary1 = dict(zip(list1,list2))
print(dictionary1)

my_dict = [('a',3),('b',4),('c',5)]
mydict = dict(my_dict)
print(mydict)

car = {
  'name' : "mahindraxuv500",
  'year' : 2024,
  'modelNo' : '2zv4'
}
print(car)
car.update({"phoneNumber":9493834674})
print(car)