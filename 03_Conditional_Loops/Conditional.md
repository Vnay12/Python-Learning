# if else in one line 

number = -2

result = "Positive" if number >= 0 else "Negative"
print(result)

syntax : we have to store it in variable and then if else live above 


# match number is like switch case in python 

number = 2 

match number: 
    case 1:
        print 
    case 2 | 3: 
        print
    case _:                 # this is default case if no other case is matched
        print     


# if conditional statement 

age = 20
if age == 20:   
    print("adult")


i = 10 
if ( i > 10):   
    pass


# if else condition 

i = 30
if( i > 20 ):
    pass
else
    pass


# if elif else 

it is used to check multiple conditions 

i = 25

 # Checking if i is equal to 10
if (i == 10):
    print("i is 10")
 # Checking if i is equal to 15

elif (i == 15):
    print("i is 15")
 # Checking if i is equal to 20

elif (i == 20):
    print("i is 20")
    
 # If none of the above conditions are true
else:
    print("i is not present")




 # Loops

 # while Loop 

 it is used to execute a block of statement until the given condition


# Python example for while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")


# while loop with continue statement

it is used when we have to skip few things in the loop 

i = 0 
a = " VINAYSURESHNAIK "

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
        
    print(a[i])
    i += 1

# while loop with break statement 

# break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
        
    print(a[i])
    i += 1



# Do While loop  *** can be implemented just like c++ *** 

# While else ( using else statment with while )

# for loop 


# for loop with string

Note:
*** in for loop we directly get access of the element meanwhile in while loop we get index ***

s = " VInay " 
for i in s: 
    print(i)


# using range with for loop 

range syntax 
range( start ,stop, step)
step is optional 


for i in range(0,10,2):
    print(i)




