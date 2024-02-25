# __init__ is a special method in class
# __init__ is a constructor
# For each object and variable will take some memory in heap memory
# Size of  an Object --> Which Objects will decide
# How much Memory will get allocated will decide how many variables are declared
# No need to call constructor explicitly it will get called automatically


class MyFunction:
  cpu = ""
  ram = ""
  def __init__(self,cpu,ram):
    self.cpu = cpu
    self.ram = ram
  def computer(self):
    print(self.cpu+self.ram)

  # def __init__(self, *args, **kwargs):

c1 = MyFunction("13","16gb")
c1.computer()
c1.computer()

class mainFunction:
  pass

num = 10
print(id(num))

class pg:
  roomNumbers = 1
  membersinRoom = 1
  eachPay = 6500
  def __init__(self):
    self.roomNumbers = 32
    self.membersinRoom = 3
    total = self.membersinRoom*self.roomNumbers
    print(total*6500)

obj1 = pg()
obj2 = pg()

obj2.membersinRoom = 54
obj2.roomNumbers = 3
obj2 = pg()






