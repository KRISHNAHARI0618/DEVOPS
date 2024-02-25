# When we are calling method from one class it will by default class local methods then it will got for parent class
# To Access parent methods also we need to use super keyword

class a:
  def __init__(self):
    print("This is A init Method")
  def feature1(self):
    print("This is Feature 1 Method")
class b(a):
  def __init__(self):
    super().__init__()
    print("This  is B init Method")
  def feature2(self):
    print("This is Feature 2 Method")

A = b()
# B = b()
