# Input: 10 
# Output :10 5 0 5 10

def printPattern(n):
    #BaseCase
    if n <= 0:
        print(n)
        return
    
    #recursivecase
    print(n)
    printPattern(n-5)
    print(n)
    

n = 10
printPattern(n)
