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

        # or code 2:

# this code using while loop 
'''
n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1

'''
