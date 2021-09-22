# Program to Print Largest Even and Largest Odd Number in a List
n = int(input("how many umber you want to enter:"))
lis = []
max_odd = []
max_even = []
for i in range(n):
    number = int(input("enter numbers:"))
    lis.append(number)
print(lis)

for j in lis:
    if j % 2 != 0:
        max_odd.append(j)
    else:
        max_even.append(j)
print("max odd in the list:", max(max_odd))
print("max even in the list:", max(max_even))


