def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0 :
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) == 0:
            result.extend(right)
            break 
        else:
            result.extend(left)
            break
        print("result:",result)
    return result


print(merge([1,4],[2,3]))