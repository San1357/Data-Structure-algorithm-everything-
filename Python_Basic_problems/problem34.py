#Program to Print the Pascal’s triangle for n number of rows given by the user

n = int(input("enter number of rows:"))
a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        print(i,j)
        a[i].append(a[i-1][j-1] + a[i-1][j])
    if n != 0:
        a[i].append(1)
for i in range(n):
    print("   "*(n-i), end=" ", sep = " ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end = " ", sep = " ")
    print()
print(a)
    



        

