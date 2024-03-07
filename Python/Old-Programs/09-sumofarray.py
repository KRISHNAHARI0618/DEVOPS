arr = [10,20,30,40,50]

print(arr[0]+arr[1]+arr[2]+arr[3]+arr[4])

sum = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]
print(sum)

# Find The largest element in the array

#Anonymoue Function

def ini(num):
    sum = num*num
print(sum)

fun = lambda b: b*b
print(fun(10))

array = [10,20,30,40,50,60,70]

len_array = len(array)

print(len_array)
sum = 0
for i in array:
    sum = sum + i
print(sum)
    # print(i)
# sum = sum + for i in array

def sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

if __name__ == "__main__":
    arr = [12,13,4,5,6,8]
    n = len(arr)
    ans = sum(arr)
    print("The sum of array is : ", ans)
    
