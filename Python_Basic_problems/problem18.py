#program to print Identity Matrix

n = int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if i == j:
            print("1" ,sep = " ", end = " ")
        else:
            print("0", sep = " ", end = " ")
    print()