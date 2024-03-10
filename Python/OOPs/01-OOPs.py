# Class : Is a group of objects having similar properties and Objects
# Objects : instances of class that are created to use the attributes and methods of class

'''
attributes are variables
behaviour are methods

what object has are : Variables / Attributes
what object does are : Methods/Functions / Behavours

'''
"""
Objects has three entities:
1: state: attributes of the object
2: behaviour: it represents methods of an objects it also reflects the responce of an object with other object
3: identity: it gives an unique name to an object and enables one object to interact with another object


class is a blue print of an object how to create a object and what object can do
class should be in pascal case,camselCase,UpperCase,_snake_case_

"""

x = 1
print(type(x))

print(type('hello'.upper()))

class Instructor:
  pass

instrutor_1 = Instructor()
print(type(instrutor_1))

# class prime:
#   def primeNumber(x):
#     for i in range(2,x):
#       if x%i == 0:
#         break
#     return x

# primeobj = prime()
# result = primeobj.primeNumber()
# print(result)

def primeNumber(x):
  for i in range(2,x):
    if x % i == 0:
      break
  return x
print(primeNumber(10))

class main:
  def __init__(self) -> None:
    print("This is Main Method Init Class")

main1 = main()
