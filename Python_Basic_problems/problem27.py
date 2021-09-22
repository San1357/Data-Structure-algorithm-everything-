# Program to Generate all the Divisors of an Integer 

n = int(input("enter any number:"))
for i in range(1, n+1):
    if n % i == 0:
        print(i)