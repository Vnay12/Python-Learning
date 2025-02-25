# print 1 to N in recursion 

def Numbers(N, i=1):
    if i > N:
        print("DONE")
        return
    
    print(i)
    Numbers(N, i+1)
    return

N = 5 
Numbers(N)