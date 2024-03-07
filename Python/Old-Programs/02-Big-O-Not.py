# Constant Run Time Complexity O(1) it is constant all the time

def Multiplication(num1, num2):
    print(num1 * num2)


Multiplication(20, 30)


# Linear Run Time Complexity as The for loop increase the Operations increases and time increases

def Print_items(n):
    for i in range(n):
        print(i)


Print_items(10)


def sum_num(n):
    if n <= 0:
        return 0
    return n + sum_num(n - 1)


print(sum_num(5))
