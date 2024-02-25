# Class is a Design/Blue Print of an Object
# Object is Instance of a Class
# Attributes are variables defined inside the Class
# Behaviour are Methods/Functions which we define inside the class

class computer:
  print("Peddireddy")
  print("Peddireddy")
  def myName(self,a,b):
    sum = a + b
    diff = a - b
    print(sum)
    print(diff)
  def myName2(self,a,b):
    print(a,b)

  def myName3(self,a,b):
    print(a*b)


com = computer()
com.myName(20,10)
com.myName2(25,10)
com.myName3(3,6)

# c = computer()
# print(c)