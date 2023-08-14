def validMountainArray(arr):
    i = 0
    length = len(arr)
    while i < length - 1 and arr[i] < arr[i+1]:
        i+= 1
    if i == 0 or i == length -1:
        return False
    while i < length - 1 and arr[i] > arr[i+1]:
        i += 1
    return i == length -1

arr = [9,8,7,6,5,4,3,2,1,0]
validMountainArray(arr)


