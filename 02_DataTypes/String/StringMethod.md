COMMON STRING METHODS

1) len()
s = " vinayNaik"
print(len(s))


2) upper() and lower()
s = " vinayNaik"
print(s.upper())
or 
print(s.lower())


3) strip()   # it removes leading and trailing whites spaces ( blank spaces)
s = "   VinayNaik   " 
print(s.strip())


4) replace()   # syntax for replace("old word", " new word" )
s = " python is fun " 
print(s.replace("fun", "easy"))


5) repeat()     # we dont have to add method name instead use multiplication sign " * " 
s = " vinaynaik"
print(s * 4)


6) title()  # for camel casing. it converts the first charc into upper and then rest lower
s = " VINAY " 
print(s.title())

7) swapcase()  # swap the cases into the opposite one 
s="VINAY"
print(s.swapcase())

8) capitalize()  # just converts the first charc of the string 
s = " we are family "
print(s.capitalize())
# output: " We are family "


9) casefold()  
# used to convert string into lower case. similar to lower() 
# if any other language is used like beta sign, alpha sign it will lower it down

s = " ß " 
print(s.casefold())

# output : " SS "  


10) center() 
it is used to center the string for example mkaing table header or something 

s1 = "hello"
s2 = s1.center(s1)
print(s2)

# output :        hello        
# there are blank spaces in width of 20 


>> we can pass length and chars to be filled 

a = "hello"
b = a.center(20, '-')  # default value is 20
print(b)

# output : -------hello--------



11) count() 
>>it returns the number of times a specified substring appears in a string
>> it is commanly used to analysis or char frequence in the string

s = " mississipiwee"
result = s.count(s)
print(result)

>> its return type is int and hence we have to store the value

>> syntax : string.count(substring, start = 0, end = len(s))
we can also mention start and end and default is starting from 0 till end 


12) encode()  


13) endswith() 
>> for checkingthe string ending with substring mentioned. 
>> it is used to check / analysis 

s = "vinaynaik"
result = s.endswith("naik")
print(result)

# output : True


14) expandtabs()


15) 