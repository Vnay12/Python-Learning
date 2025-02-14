# finding the length of string 

# Using inbuit function
a = "vinay"
print(len(a))

# using for loop
a="Vinay"
count = 0

for i in a:
    count+=1
print(count)


# using inbuilt string funtion 

a ="Vinay"
answer = a.count("") - 1
print(answer)


# using while loop 

a="vinay"
count = 0
while count < len(a):
    count +=1
print( count )