# This is Absoulute build in functions

print(abs(-23.8733))

print(abs(34.7777))

print(round(34.777))

print(round(34.23))

myList = [False,True,True]
x = all(myList)
print(x)

# for _ in range(0,10):
#   if all:
#     print(True)
#   else:
#     print(False)

# all --> will give the all the elements in the list should be true then it will give true else false

myList = [1,1,1]
x = all(myList)
print(x)

# Any --> any element should be true

myList = [0,1,0]
x = any(myList)
print(x)

x = ascii("My Name is Peddireddy")
print(x)

# Bin function will gives the binary function for an integer it will always start with 0b

x = bin(20)
print(x)

for i in x:
  print(i)

# Bool Is an Object with an error
x = bool(1)
print(x)
y = bool(0)
print(y)

z = bool(10)
print(z)

x = bytearray(10)
print(x[-2])

byte_array = bytearray([65, 66, 67])
byte_data = bytes(byte_array)

# Creating bytes objects
empty_bytes = bytes()
byte_values = bytes([65, 66, 67])  # ASCII values for 'A', 'B', 'C'
text = "Hello, World!"
byte_data = bytes(text, encoding='utf-8')

# Displaying the results
print("Empty Bytes:", empty_bytes)
print("Bytes from values:", byte_values)
print("Bytes from text:", byte_data)
