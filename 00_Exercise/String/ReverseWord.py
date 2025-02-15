# Reverse words order in a string   


# using spilt and join 


a = " vinay is a good boy"
words = a.split()   # this will split the words into list of words default taking space
reverse_word=words[::-1]  # this will reverse using slice
print(reverse_word)  # this is reverse but theyt are not a single sentence

join_word = " ".join(reverse_word) # we use join to make it in single sentence
print(join_word)



# using for loops 

a = "Vinay is a good boy"

words = a.split()
reverse_words_list = []

for i in range(len(words)- 1, -1, -1 ):
    reverse_words_list.append(words[i])
result = " ".join(reverse_words_list)


# using stack 

# using recursion

#using two pointer

a = "vinay is a good boy"
splitstring = a.split()
n = len(splitstring)
left, right = 0, n - 1


while left < right:
    temp = splitstring[right]
    splitstring[right] = splitstring[left] 
    splitstring[left] = temp 
    right -= 1 
    left += 1
print(splitstring)

answer = " ".join(splitstring)
print(answer)



