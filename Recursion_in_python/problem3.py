def fibo(n):
    #Base case
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

n =10
print(fibo(n))
