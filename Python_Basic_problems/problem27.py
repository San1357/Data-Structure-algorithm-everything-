# Program to Generate all the Divisors of an Integer 

n = int(input("enter any number:"))
divisor = [] 
for i in range(1, n+1):
    if n % i == 0:
        divisor.append(i)

print("The divisor of the no.", n, "are:", divisor)