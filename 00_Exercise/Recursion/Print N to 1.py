# Print N to 1 recursive

def Numbers(N,i):
    if i < 1:
        print("DONE")
        return
    
    print(i)
    Numbers(N, i-1)
    return

N = 5
Numbers(N, N)