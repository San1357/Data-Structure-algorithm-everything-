#check if a number is armstrong number

#Armstrong Number: 1634
# ex: (1**4) + (6**4) + (3**4) + (4**4) => 1634

armst = 0
number = input("enter any number:")
for i in number:
    armst = armst + int(i) ** len(number)
print(armst)
if int(number) == armst:
    print("It is Armstrong number.")
else:
    print("It is not Armstrong number.")



