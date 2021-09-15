#find sum of digits of a +ve integer no. using recursion

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'the no. shoulde be positive integer'
    if n== 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10) 

        
print(sum_of_digits(0))