# Given a number ‘N’, find out the sum of the first N natural numbers.


def sum(N, i=0, count = None):
    if count == None:
        count = 0

    if i > N:
        print("DONE")
        return
    
    count = count + i
    sum(N, i+1)
    return count

N = 5
print(sum(N))

