#program to compute prime factors of an integer

primefactors = []
def factor(n):
  for i in range(2,int(n//2)+1):
    prime = True
    for j in range(2,int(i**.5)+1):
        print(i,j)
        if i%j == 0:
            prime = False
            break
    if prime and n%i == 0:
      primefactors.append(i)
  print ("primefactors is :",primefactors)

factor(98)