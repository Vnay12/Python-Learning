# This is string slicing 
name = "Vinay"
print(name[2:4])

name = "python"
print(name[::-1])


# string immutability using slice
name = "vinay"
name2 = "p" + name[1:]
answer = name2 
print(answer)


# converting string into list and then back to string

name = "vinay"
name_list = list(name)  # this will convert into list
name_list[0] = "P"
name = "".join(name_list)   # this will convert into string
print(name)





