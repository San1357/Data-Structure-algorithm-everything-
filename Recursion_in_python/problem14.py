#a = [1,2,3,[4,5]]

def flatten(arr):
    result = []
    for custItem in arr:
        if type(custItem) is list:
            result.extend(flatten(custItem))
        else:
            result.append(custItem)
    return result

arr = [1,2,3,[4,5,[6]]]
print(flatten(arr))
