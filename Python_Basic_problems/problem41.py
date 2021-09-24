# area of Triangle given all three sides .
import math
sides1 = int(input("enter side 1:"))
sides2 = int(input("enter side 2:"))
sides3 = int(input("enter side 3:"))

s = (sides1 + sides2 + sides3)/2 # s -> semi perimeter
area = math.sqrt(s*(s-sides1)*(s-sides2)*(s-sides3))
print(area)
