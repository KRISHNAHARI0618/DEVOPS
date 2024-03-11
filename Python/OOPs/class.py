# Class : Design(BLUE Print)

# Object : Instance of a Class

# Attribute : Variables

# Behavour : Methods/Functions

# object = Class() : This is Constructor

# Arguments : The Variables which will be passed inside the Method is called Arguments eg:... def main(self,arg1,arg2,arg3):

# __init__(self) is a Contructor is called as soon as the object class is instantiated

# Variables : Class Variables & Instance Variables

# Instance Variables : Variables Declared inside the method is called Instance Variables

# Types of Methods:
'''
1: Instance Method
2: Class Method
3: Static Method

'''
class pg:
  def __init__(self,name,floorNo,roomNo,year):
    self.name1 = name
    self.floorNo1 = floorNo
    self.roomNo1 = roomNo
    self.year1 = year
    print(name,floorNo,roomNo,year)

pg1 = pg("hari","1st","105","2024")
pg2 = pg("reddy","2nd","108","2023")
print(pg1.name1)

class Computer:
  def main(self):
    print("HP",'i5',32000)

  def main2(self):
    print("Lenovo","i5",45000)

com = Computer()
com.main() # This also represents which object should behave
com.main2()

Computer.main(com) # This represents which object should behave

class Car:
  def model1(self):
    print("Audi",2024,10000)
    print("Benz",2023,15000)
  def model2(self):
    print("RollsRoyce",2025,34000)
    print("Sumoto",2026,45000)

mod1 = Car()
mod1.model1()
mod1.model2()

mod1 = Computer()
mod1.main()
mod1.main2()

class Car1:
  def __init__(self,name,price,modelNo,year):
    self.price = price
    self.modelNo = modelNo
    self.year = year
    self.name = name
    print(name,price,year,modelNo)

com = Car1("Audi","$240000","2024","AU243") # This is Called Constructor
# com.model("Audi","$240000","2024","AU243")


