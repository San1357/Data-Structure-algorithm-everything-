#program to check if a number is palindrome or not
n = 4321
s = str(n)
for i in range(0, len(s)):
    if s[i] != s[len(s)-i-1]:
        print("its not palindrome")
        break
else:
    print("palindrome")
        
        
