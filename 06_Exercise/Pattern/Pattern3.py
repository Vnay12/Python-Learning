'''

1
12
123

'''

input = int(input("Enter the number:"))
print(input)

for i in range(input):
    for j in range(i+1):
        print(j+1, end="")
    print()
        

