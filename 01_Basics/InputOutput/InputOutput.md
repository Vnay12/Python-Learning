Input

1) To take input we can use input() function
 >> x = input("Enter the value:" )

 2) input() function returns value in string by default so we can use string methods on it for further uses

 3) to make the string to any other data type we have typecast 
 >> answer = input("enter your age:")
    age = int(answer)
    if age < 0:
    print("not born")

4) we can directly typecast in one line while taking input 
    >> age = int(input("Enter your age:"))
        print(age)

