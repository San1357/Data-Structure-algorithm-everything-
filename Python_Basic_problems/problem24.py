#program to read Height in cm & then convert height to feet & inches.
height = float(input("enter height in cm:"))
height_in_feet_inches = height * 0.0328084
a = str(height_in_feet_inches)
feet, height =  a.split('.')
print("your height in feet & inches is:", feet,"" +"feet" + ",", height, " " +"Inches")
