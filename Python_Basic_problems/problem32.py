# program to find those number which are divisible by 7 and multiple of 5 in a given range of numbers 

upper_range = int(input("enter upper range:"))
for  i in range(1, upper_range+1):
    if i % 5 == 0 and i % 7 == 0:
        print("The numbers are:",i)



