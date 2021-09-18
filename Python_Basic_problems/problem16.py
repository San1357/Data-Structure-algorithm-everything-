# Program to Read a Number n And Print the Series “1+2+…..+n="

n = int(input("enter number:"))
for i in range(1,n+1):
    a = []
    for j in range(1, i+1):
        print(i, sep = '', end = '')
        if j<i:
            print("+",sep = '', end = '')
        a.append(j)
    print("=",sum(a))

print()

