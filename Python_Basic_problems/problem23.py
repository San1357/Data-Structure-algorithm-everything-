#program to check given year is a leap year or not.

leap_year = int(input("enter year:"))
if leap_year % 4 == 0 or leap_year % 400 == 0:
    print("It is leap_year")
else:
    print("It is not leap year")
    
