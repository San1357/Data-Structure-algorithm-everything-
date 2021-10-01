# program to find the LCM of two numbers 
n1 = int(input("enter first number:"))
n2 = int(input("enter 2nd number:"))
if n1> n2:
    min1 = n1
else:
    min1 = n2
while(1):
    if(min1 % n1 == 0 and min1 % n2 == 0):
        print("LCM is:", min1)
        break
    min1 = min1+1

