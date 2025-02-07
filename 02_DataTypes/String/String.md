1) Creating a string with " "

2) Multi line string """  """

3) to directly access python string 
>> name = "Vinay" 
    print(name[2])

>> Negative indexing     *** will do later *** 

4) slicing is a way to extract portion of a string by specifing start and end indexes. end is stoppping index excluded 
>> name = "VinayNaik"
    print(name[2:4])        # it will print " na " 

>> Slicing syntax is 
    oject name = s[start : end : step]
    s = original string name 
    start = from where we want to start
    end = till where we want to get the string ( one step ahead of the end index)
    step = if we want to skip and hop for example 2 2 steps 

>> return of this is always string as we are doing it on string 

>> we can also reverse the string by keeping the step value -1 
    name = python 
    print(name[::-1])

    # default value of step is 1 and when it make it -1 it will start from the left this is negative indexing 


5) String Immutability 
>> if we have to manipulate string we have make new string and then use slice() or concatenation or formatting 


>> Benefits of Immutable objects: 
    1) Hashability and Dictionary keys :- Immutable objects can be used as keys in dictionaries because their hash value remains constant, ensuring that the key-value mapping is consistent.

    2) Memory Efficiency: Since immutable objects cannot change their value, Python can optimize memory usage. Reusing the same immutable object across the program whenever possible reduces memory overhead.

    3) Thread Safety: Immutability provides inherent thread safety. When multiple threads access the same immutable object, there’s no risk of data corruption due to concurrent modifications.

    4) Predictability and Debugging: With immutability, you can be confident that a given object’s value will not change unexpectedly, leading to more predictable and easier-to-debug code.

    5) Performance Optimization: Immutable objects facilitate certain performance optimizations, such as caching hash values for quick dictionary lookups.


>> ways to deal with string immutability 

    1) String Slicing and Reassembling
    2) String Concatenation
    3) the join() method
    4) Using String Formatting
    5) Converting to Mutable Data Structures


>> we can convert immutable data type into mutable also one such example 
    # converting string into list

    s = " vinay " 
    new s = list(s) # this has converted into list
    new s[0] = " V " 
    new string = "".join(new s)  # this will again convert it into string
    print(new string)

    