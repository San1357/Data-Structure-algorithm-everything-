#write a recursive function called someRecursive which accepts an array and a callback. The funcn 
# return true if a single value in the array returns true when passed to the callback. otherwise
# it return false.



def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
print(someRecursive([2,3,6] ,isOdd))

