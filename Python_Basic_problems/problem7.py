# print all numbers in a range divisible by a given number.

range1 = int(input("enter the range1:"))
range2 = int(input("enter the range2:"))
n = int(input("enter the number to be divide by:"))
for i in range(range1, range2):
    if (i%n == 0):
        print(i)
