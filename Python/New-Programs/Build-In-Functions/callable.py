from typing import Any


def x():
  a =  5

print(callable(x))

# Call and Callable
# Callable functions will give true if the object/function is callable else it will be false


class main:
  def main_method(x):
    print(f"{x}, Hello world")

c1 = main()
c1.main_method()
print(callable(main.main_method(10)))

class car:
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    pass