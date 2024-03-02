'''
numbers = [1, 0, 2, 0, 3, 4, 0, 5]

filtered_numbers = [num for num in numbers if num != 0]

print(filtered_numbers)


def move_zeros_inplace(numbers):
    for num in numbers:
        if num == 0:
            numbers.remove(num)
            numbers.append(0)

# Example usage:
original_list = [0, 2, 0, 3, 4, 0, 5, 0]
move_zeros_inplace(original_list)

print("List with Zeros Moved to the End (In-Place):", original_list)
'''


list_numbers = [0,2,3,4,0,9,5,0,8,0,5]

print(list_numbers)

for i in list_numbers:
  if i == 0:
    list_numbers.remove(i)
    list_numbers.append(0)
print(list_numbers)
