class main:
  def __init__(self):
    self.name = "Peddireddy"
    self.age= 25

  def compare(self,other):
    if self.age == other.age:
      return True
    else:
      return False

c1 = main()
print(c1.age)

c1.age = 45

c2 = main()

if c1.compare(c2):
  print(c1.age,"I am Same")
else:
  print(c1.age,"I am Different")