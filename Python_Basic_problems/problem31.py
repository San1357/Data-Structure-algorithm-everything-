# program to form an integer that has the number of digits at ten's place and the least significant
# digit of the entered integer at one place.

number = input("enter the number:")
for i in number:
    if i == number[-1]:
        print(str(len(number))+str(i))

       
        # OR code 2nd

 
    #using while loop
'''
n=int(input("Enter the number:"))
tmp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("The new number formed:",int(d))
'''
        
