# Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
n = int(input("how many numbers you want to integer:"))
lis = []
odd = 0
even = 0
negative = 0
for i in range(n):
    numbers = int(input("enter any integer of any types:"))
    lis.append(numbers)
print(lis)
for j in lis:
    if j < 0:
        negative = negative + j
        
    elif j % 2 != 0:
        odd = odd + j
        
    else:
        even = even +j
print("Odd:",odd)
print("negative:",negative)
print("even:",even)


