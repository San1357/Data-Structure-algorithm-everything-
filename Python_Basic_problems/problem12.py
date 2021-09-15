# Program to Find the Smallest Divisor of an Integer
n = 53
for i in range(2,n+1):
    if n%i == 0:
        print(i)
        break
    