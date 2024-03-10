class main:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    print(name,year)
  def display(self,language):
    print(f"I am Learning {language}")

class_1 = main("peddireddy",9493834674)
class_1.display("python")
# print(class_1)


class car:
  def car_method(self):
    print("This is Car Class")
class bus:
  def bus_method(self):
    print("this is bus method")
    print("This is bus class")
class train:
  def train_method(self):
    print("This is train class")
    print("This is Train Method")

class car(train):
  def car_train_method(self):
    print("This is Main inherited class for car and train")

c1 = car()
c1.car_train_method()
c1.train_method()
