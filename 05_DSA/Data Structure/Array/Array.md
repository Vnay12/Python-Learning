1) Declaration of array 
arr = []

2) initialization of array 

arr = [1,2,3,4,5]


3) two types of array 
    a) fixed size array 
    arr[0] * 5
    b) dynamic suze array 
    arr=[]

    c) 1D array
    d) Multi dimension array


4) traversal in array 

a) linear 

arr = [1,2,3,4,5,6]
for i in arr:
    print(i)

b) reverse 

arr = [1,2,3,4,5,6]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])

    
5) searching in arrray 

a) linear

arr = [34,234,5,1,1,235,132,4]
target = 4
for i in range(len(arr)):
    if target == arr[i]:
        print("found")
    else:
        print("not found")


6) modifying element in array


arr = [10, 20, 30, 40, 50]

# Modifying elements using traversal (increasing each by 5)
for i in range(len(arr)):
    arr[i] += 5

# Print modified array
print("Modified array:", end=' ')
for num in arr:
    print(num, end=' ')
print()


7) insert in array

a) identify the positioon where to insert an element
b) shift element one step forward 
c) insert the element
d) updat the size 

3 types of insertion 

a) at beginning
b) at specific location 
c) at the end of the array


A) At the beginning of the array

Approch 1 : using built in method insert()

arr =[1,3,4,5,6]
arr.insert(0,6)


Approch 2 : using custom method 


2) Insert at specific index 

Approch 1 : using built in method 

# we have to ask user where to and then use insert()
# for example a user wants to insert at 3

arr = [1,2,3,4,5]
pos = 3

arr.insert(pos-1, 4)


Approch 2: Using custom method 


# Python program to insert given element at a given position
# in an array using custom method

if __name__ == "__main__":
    n = 4
    arr = [10, 20, 30, 40, 0]
    ele = 50
    pos = 2
    print("Array before insertion")
    for i in range(n):
        print(arr[i], end=' ')

    # Shifting elements to the right
    for i in range(n, pos - 1, -1):
        arr[i] = arr[i - 1]

    # Insert the new element at index pos - 1
    arr[pos - 1] = ele

    print("\nArray after insertion")
    for i in range(n + 1):
        print(arr[i], end=' ')


