def OneDigit(num):
    return ((num>=0) and (num<10))

def isPal(num,duplicate):
    if OneDigit(num):
        return (num == (duplicate[0])%10)
    if not isPal(num//10, duplicate):
        return False
    
    duplicate[0] = duplicate[0]//10

    return (num % 10 == (duplicate[0]) % 10)

def isPalp(num):
    if (num<0):
        num = (-num)
    duplicate = [num]
    return isPal(num,duplicate)

n = 1
OneDigit(n)


