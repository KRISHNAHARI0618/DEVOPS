def main(x,y):
  print(x,y)
  try:
    print(y/0)
  except ZeroDivisionError as e:
    print(f"This is {e}")

main(10,20)

x = 5

try:
  assert x == 10
except AssertionError as e:
  print(f"This is {e}")