s = 'nitin'
for i in range(0, int(len(s)/2)): #time: O(n/2)) , #space: O(n)
    print(i)
    if s[i] != s[len(s)-1-i]:
        print( False)
        break
print(True)



