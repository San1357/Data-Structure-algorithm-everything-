'''def recursive_Funcn():
    if <basCase_Condition>:
        return some base case value 
    else:
        return <recursive call and other task>'''

def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)


n = 4
print(factorial(n))