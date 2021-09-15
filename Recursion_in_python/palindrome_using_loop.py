Input = "nitin"
check = ""
for i in Input:      # time: O(n)
    check = i+ check # space: O(n)
    print(i,check)
if check == Input:
    print("palindrome")
else:
    print("Its not")


