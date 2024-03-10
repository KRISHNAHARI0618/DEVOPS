for i in range(97,122):
  print(chr(i),end=" ")
for i in range(67,91):
  print(chr(i),end=" ")

# Class method converts a method into a class method
def main(x,y):
  print(x,y)

main(10,20)

class main:
  class_variables = "Peddireddy"
  def __init__(self) -> None:
    pass
  @classmethod
  def class_method(self,x,y):
    print(f"{x,y} There are Method Variables, {main.class_variables} is my name")
  def class_method2(self,x,y):
    print(f"{x,y} {main.class_variables}")

c1 = main()
c1.class_method(20,30)
c1.class_method2(20,30)

x = format(0.5,".2%")
print(x)