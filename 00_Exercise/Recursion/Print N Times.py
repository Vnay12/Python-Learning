# using recursion print name n times 


def printName(name, N, i = 0):
    while i < N:   # base condition 
        print(name)
        printName(name, N, i+1)
        return
    print("DONE")


name = "VINAY"
N = 3 

printName(name, N)