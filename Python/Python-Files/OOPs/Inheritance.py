# Inheritance==> Taking the features from the parent class
# There are three types of inheritance
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance

class A:
  def feature1(self):
    print("Feature 1 is Working")
  def feature2(self):
      print("Feature 2 is Working")
class B:
  def feature3(self):
    print("Feature 3 is Working")
  def feature4(self):
      print("Feature 4 is Working")
class C(A,B):
  def feature5(self):
    print("Feature 5 is Working")
  def feature6(self):
    print("Feature 6 is Working")

# class C:
#   def feature3(self):
#     print("Feature 3 is Working")

# C1 = A()
# C2 = B()
# C3 = A()
# C1.feature2()
# C2.feature2()
# C3.feature1()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()