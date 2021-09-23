Input = "aayushyaa"
flag1 = -1
flag = 0
for i in Input:         #time : O(n)
    print(i)            # space: O(n)
    if i != Input[flag1]:
        flag = 1
        break
    flag1 = flag1 -1

if flag == 1:
    print("no")
else:
    print("yes")