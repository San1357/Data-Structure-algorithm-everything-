#find GCF

def gcd(no1, no2):
    assert int(no1) == no1 and int(no2) == no2, 'the no. should be integer'
    if no1<0:
        no1 = -1*no1
    if no2<0:
        no2 = -1 * no2
    if no2 == 0:
        return no1
    else:
        return gcd(no2, no1%no2)

print(gcd(48,18))