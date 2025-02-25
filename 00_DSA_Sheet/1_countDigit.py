# Problem Statement: Given an integer N, return the number of digits in N.

# Iterative approch 

digit = int(input("Enter the number:"))
count = 0
for i in range(digit):
    count +=1
print(count)