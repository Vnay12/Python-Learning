# Find the Largest element in an array

arr = [1,2,3,4,5]
n = len(arr)
max = 0
for i in range(n):
    if arr[i] > max:
        max == arr[i]
        i+=1
    elif arr[i] <= max:
        i+=1
print(max)