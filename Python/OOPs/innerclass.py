# from turtle import color


class main:
  def MainFunc(self,x,y):
    self.x = x
    self.y = y
    print(self.x,self.y)
class child:
  def childFunc(self,x,y):
    self.x = x
    self.y = y
    print(self.x,self.y)
  innerClass = main()

c1 = child()
# c1.c1
c1.innerClass.MainFunc(30,40)
c1.childFunc(40,50)


class Color:

  def __init__(self):
    self.name = 'Green'
    # self.lg = self.LightGreen()

  def show(self):
    print('Name: ', self.name)

class LightGreen:
  def __init__(self):
    self.name = 'Light Green'
    self.code = '024Cva2'
  def display(self):
    print('Name : ',self.name)
    print('Code: ', self.code)
  outer = Color()

c1 = LightGreen()
c1.display()

