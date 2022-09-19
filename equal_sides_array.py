def equal_array(arr):
    # if len(arr) <= 0:
    #     return -1
    for i in range(len(arr)):
        if sum(arr[0:i]) == sum(arr[i+1:]):
            return i
    return -1

print(equal_array([1,2,3,4,5,6,5,4,3,2,1]))
