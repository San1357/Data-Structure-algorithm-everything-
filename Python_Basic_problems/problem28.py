#program to print table of given number 

n = int(input("enter any number:"))
for i in range(1,11):
    if n > 0: 
        mul = n* i
        print(str(n) + "*" + str(i) + "  :", mul)
