# Python Program to Calculate the Average of Numbers in a Given List
length = int(input("enter the length of list:"))
lis = []
for i in range(0,length):
    elements = int(input("enter the no.:"))
    lis.append(elements)
print(lis)

sum = 0
for i in range(0, len(lis)):
    sum += lis[i]
    average = sum//length
print(average)

