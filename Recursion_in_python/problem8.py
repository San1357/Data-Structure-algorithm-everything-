#Calculate power of no. using recursion

def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'the no. should be Postive integer' 
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

print(power(-2,2))