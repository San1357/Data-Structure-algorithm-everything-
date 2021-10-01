#program to print an Inverted Star pattern

n = int(input("enter no. of rows:"))
for i in range(n,0,-1):
    print((n-i)* ' ' + i * '*')
