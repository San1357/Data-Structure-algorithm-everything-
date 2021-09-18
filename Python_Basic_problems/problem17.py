# Program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes
n = int(input("enter upper limit of range:"))
sieve = set(range(2, n+1)) # 2, 3, 4, 5, .....n
while sieve:
    prime = min(sieve)
    print(prime, end = "\t")
    sieve-= set(range(prime,n+1,prime))
else:
    print()
