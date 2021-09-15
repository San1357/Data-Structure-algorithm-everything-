def is_palindrome(s):
    l = len(s)
    i = 0

    if l < 2:
        return True
    elif s[i] == s[l-1]:
        return is_palindrome(s[i+1:l-1])   # time: O(n/2) or O(n) 
                                           # space: O(n)
    else:
        return False

s = "NITIN"
ans = is_palindrome(s)

print("palindrome") if ans else print("no")

