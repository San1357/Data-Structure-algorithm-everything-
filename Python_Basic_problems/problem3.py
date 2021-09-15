#program to read a number n and compute n+nn+nnn
n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
print(t1)
t2=temp+temp+temp
print(t2)
comp=n+int(t1)+int(t2)
print("The value is:",comp)
