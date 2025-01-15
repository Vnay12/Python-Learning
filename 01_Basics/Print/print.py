
""" 

1) what is print() function?

>> The print() function prints the specified message to the screen, or other standard output device.

>> Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

>> object(s) : Any object, and as many as you like. Will be converted to string before printed
>> sep=separator : Specify how to separate the objects, if there is more than one. Default is ' '
>> end=end : Specify what to print at the end. Default is '\n'
>> file : An object with a write method. Default is sys.stdout
>> flush : A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False



 """








# this is a simple print statement
print("Hello, world!")

# this is passing a value to the print function
name = "John"
print(name)

# this is passing multiple values to the print function
name = "John"
age = 23
print(name, age)

# this is passing multiple values to the print function with a separator
day = 12
month = 9
year = 2000
print(day, month, year, sep=" - ")


# this is passing multiple values to the print function with a separator and an end
# end is used to specify what to print at the end of print () function
# by default if it is not specified, it will print a new line " \n"

day = 12
month = 9
year = 2000
print("Date of birth", end=" ")
print(day, month, year, sep=" - ")


# print() function with file parameter
# file parameter is used to write the output to a file

print("Hello, File Output Check!", file=open("E:\Coding Files\Python\Python-Learning\Supplements\output.txt", "w"))



# this is using f-string to print the values formatted in a string
name = "Alice"
age = 30
print(f"Enter your name: {name}, Enter your age: {age}")



# print () function for printing objects.... ill do that once i learn about class and objects in python