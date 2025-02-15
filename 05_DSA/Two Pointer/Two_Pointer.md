Explaination:

1) As the name suggest two pointer uses two pointers to find the answer to a problem in the optimal time 
2) when the input data is given linear form we can use two pointer 
3) linear data - array, list, linked list etc
4) this approch is usefull when you want to reduce time complexity

Pattern:-

1) it can be used when you want to process two elements in a single iteration or determine a type of pattern
2) example : checking palindrome in array, list, string 
3) detection loop in a linked list 
4) reverse a string
5) find the middle element etc

Q) Given an array, find the indexes of two elements whose sum is equal to the given sum. If there exist multiple solutions, print the minimum indices.

Example 1:

Input: arr[]={1,3,4,5,7,10,11,19,20}, sum=7
Output: {1,2}

Example 2:
Input: arr[]={2,9,13,21,54}, sum=63
Output: {1,4}

A) 
1) here we have to assume array is sorted ( if not then sort the arrray )
2) this is brute force method 

def twosum( arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return true
    return false

if __name__ == "__main__":
    arr=[0,1,2,3,4,5]
    target=8

    if twosum(arr,target):
        print(true)
    else:
        print(false)

Time complexity will be O^2


3) This is 2nd approch ( a better approch )

Binary search and Hashing


4) two pointer technique is the best to solve such questions 

def twopointer(arr, target):
    arr.sort()
    n = len(arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] = arr[right]

        if sum == target:
            return true
        elif sum < target:
            left +=1
        elif sum > target:
            right -=1
            
    return false
        
