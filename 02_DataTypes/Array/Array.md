NumPy array are a part of numpy for numerical computqation in python.

Numpy array advantages 

1) Multi-dimensional support: NumPy arrays can handle more than one dimension, making them suitable for matrix operations and more complex mathematical constructs.
2) Broad broadcasting capabilities: They can perform operations between arrays of different sizes and shapes, a feature known as broadcasting.
3) Efficient storage and processing: NumPy arrays are stored more efficiently than Python lists and provide optimized performance for numerical operations

import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4])

# Element-wise operations
print(arr * 2)  

# Multi-dimensional array
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d * 2)



# Creating Array in python 

Array in Python can be created by importing an array module. array( data_type , value_list ) is used to create array in Python with data type and value list specified in its arguments.


import array as arr

arr1 = arr.array(['i', [1,2,3]])

for i in rang(0,3):
    print(arr1[i])


# adding element to array 

import array as arr

array1 = arr.array('i',[1,2,23])
print(*array1)

array1.insert(4)
print(*array1)


# to know the datatype of array 

typecode

# importing "array" for array operations
import array
	
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 

# using typecode to print datatype of array
print ("The datatype of array is : ")
print (arr.typecode)


# to convert array to list = tolist()

# importing "array" for array operations
import array
	
# initializing array with array values
arr = array.array('i',[1, 2, 3, 1, 2, 5]) 

# using tolist() to convert array into list
li2 = arr.tolist()

# printing the new list
print ("The new list created is : ",end="")
for i in range (0,len(li2)):
	print (li2[i],end=" ")
