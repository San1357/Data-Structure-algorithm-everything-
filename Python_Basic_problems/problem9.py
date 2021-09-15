#program to accept three digits and print all possible combination from digits 
#example :
# Input: 1 2 3
#     Output:
#         1 2 3
#         1 3 2
#         2 3 1
#         2 1 3
#         3 1 2
#         3 2 1 

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d = []
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
                