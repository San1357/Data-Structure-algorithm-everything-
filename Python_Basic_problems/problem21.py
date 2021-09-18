# Program to Check if a Date is Valid and Print the Incremented Date if it is

date = input("Enter the date:")
print(date)
dd,mm,yy = date.split('/')
dd = int(dd)
mm = int(mm)
yy = int(yy)
print(dd)
print(mm)
print(yy)
if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    max1 = 31
elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    max1 = 30
elif mm == 2 and (yy%4 == 0 or yy%100 != 0 or yy % 400 == 0):
    max1 = 29
else:
    max1 = 28
if (mm<1 or mm>12):
    print("Date is invalid")
elif (dd<1 or dd > max1):
    print("Date is invalid")
elif dd == max1 and mm != 12:
    dd = 1 
    mm = mm+1
    print("The incremented date is:", dd, mm, yy)
elif dd == 31  and mm == 12:
    dd = 1
    mm = 1
    yy = yy + 1
    print("the incremented date is:", dd,mm,yy)
else:
    dd = dd+1
    print("the incremented date is:", dd ,mm, yy)



