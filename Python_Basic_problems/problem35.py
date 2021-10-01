# Check if a Number is a Perfect Number
n = int(input("enter any number:"))
sum1 = 0
for i in range(1,n):
    if n % i == 0:
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a perfect number")
else:
    print("NO, It is not a perfect number.")
