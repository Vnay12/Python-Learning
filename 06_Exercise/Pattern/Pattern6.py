'''

  *
 * *
* * *

'''

input = int(input("Enter the number:"))
print(input)

for i in range(1,input+1):
    for j in range(i,2*input-1):
        print("*", end="")
    print()
        

