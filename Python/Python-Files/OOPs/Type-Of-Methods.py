# Accessors : if you want just fetch the values from the method is called Accessors
# Mutators: If you want to modify the values in methods then it is called Mutators
# Decorator: @classmethod when we are using class variables
# Static Variables: When we are using static variables @staticmethod


class Student:
  school = 'Telusko'
  def __init__(self,m1,m2,m3):
    print("Hello World")
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  def avg(self):
    print((self.m1+self.m2+self.m3)/3)
  @classmethod

  def info(cls):
    print("@class method")

s1 = Student(20,30,50)
s1.avg()
s1.info()
# print(s1.avg())
