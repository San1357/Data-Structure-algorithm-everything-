# check if a no. is strong number or not.
# Strong /Number : Ex1 - 234 = 2! + 3! + 4! => 2 + 6 + 24 => 32 is not equal to 234 (Not Strong number.)
#                  Ex2 - 145 = 1! + 4! + 5! => 1+ 24 + 120 => 145 == 145 (Strong number)

n = int(input("enter any number"))
sum1 = 0
temp = n
while(n):
    i = 1
    f = 1
    r = n % 10
    print(r) 
    while (i<=r):
        f = f*i
        i = i+1
    sum1 = sum1 + f
    n = n//10
print(temp)
if(sum1 == temp):
    print("The number is Strong number.")
else:
    print("The number is not a strong number")
  