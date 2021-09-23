# program to form an integer that has the number of digits at ten's place and the least significant
# digit of the entered integer at one place.

number = input("enter the number:")
for i in number:
    if i == number[-1]:
        print(str(len(number))+str(i))
