#convert decimal to binary using recursion
def convert(decimal):
    assert int(decimal) == decimal, 'the decimal should be integer only'
    if decimal == 0:
        return 0 
    else:
        return decimal % 2 + 10 * convert(decimal//2)

print(convert(10)) #1010

