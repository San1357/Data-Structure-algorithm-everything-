# write a recursive function called isPalindrome which return true if the string passed to it is a palindrome,
# otherwise return False

#string = 'aja'
 
def isPalindrome(string):

    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    else:
        return isPalindrome(string[1:-1])

print(isPalindrome('nitin'))
        