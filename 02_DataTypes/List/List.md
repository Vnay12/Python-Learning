1) List are dynamic 
2) they are mutable and they can be manupilated

a = [10,20,30]
print(a[0]) # access first index item 

a.append(11) # it will add item 
a.remove(20) # remove item 

# using list constructor 

 s = " vinay " 
new s = list(s) # this has converted into list
new s[0] = " V " 
new string = "".join(new s)  # this will again convert it into string
print(new string)

# adding element into list 

1) append method 

it is used to add single item to the end of the list and it doesnt return new list instead it will modify the exisiting list 

a = [2, 5, 6, 7]

# Use append() to add the element 8
# to the end of the list
a.append(8)
print(a)

A) append list to list 
a = [1, 2, 3]

a.append([4, 5])
print(a)

# output : [1, 2, 3, [4, 5]]


2) extend method 

it is used to add items from one list to the end of another list 

a = [1, 2, 3]
b = [4, 5]

# Using extend() to add elements of b to a
a.extend(b)

print(a)

# output : [1, 2, 3, 4, 5]

( note : this is best method to append list to list or say concat two list )


3) insert method

insert will insert item at specific index 


# creating a list

fruit = ["banana","cherry","grape"]
fruit.insert(1,"apple")
print(fruit)



# removing element from the list

1) list remove() method 

it will remove the first occurance of the given item form the list 
it will take only 1 argument

a = ['a', 'b', 'c']
a.remove("b")
print(a)


2) to remove all the values from the list 

A) List comprehension    *** will do later *** 
B) filter( ) and lamba   *** will do later ***
C) Looping thr list manually 

a = [1, 2, 3, 4, 5]
b = [2, 4]

# Manually looping through 'a' to remove values present in 'b'
result = []
for item in a:
    if item not in b:
        result.append(item)

# Output the result
print(result)

D) using remove( )

a = [1, 2, 3, 4, 5]
b = [2, 4]

# Removing elements from 'a' that are in 'b'
for item in b:
    while item in a:
        a.remove(item)

# Output the result
print(a)


2) list pop( ) method 
it is used to pop the element at the specific index 
if not given the index it will remove the last element 

a = [10, 20, 30, 40]

# Remove the last element from list
a.pop()

print(a)



# Iterate over a list in python 

1) using for loop and range()

a = [1, 3, 5, 7, 9]
 
# Calculate the length of the list
n = len(a)
 
# Iterates over the indices from 0 to n-1 (i.e., 0 to 4)
for i in range(n):
    print(a[i])



2) using while loop 

a = [1, 3, 5, 7, 9]
 
# Start from the first index
i = 0
 
# The loop runs till the last index (i.e., 4)
while i < len(a):
    print(a[i])
    i += 1


3) using enumerate()  

a = [1, 3, 5, 7, 9]

# Here, i and val reprsents index and value respectively
for i, val in enumerate(a):
    print (i, val)



# to get list as input from user 

1) using spilt( ) method 

# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()

print("List:", user_input)


2) using loop 

a = []

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Append elements to the list
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("List:", a)


3) Using map()   *** will study later ***



