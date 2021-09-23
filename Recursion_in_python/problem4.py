def sum1ton(n):
    #base case
    if n == 1:
        return n
    else:
        return(n+sum1ton(n-1))

n = 5
print(sum1ton(n))