def is_palindrome(s):
    return s == s[::-1]   # time : O(n)
                          #space: O(n)
s = "aura"
ans = is_palindrome(s)
if ans:
    print("ha bhai palindrome hai")
else:
    print("chal saale dusra string leke aa E palindrome Naikhe baa")