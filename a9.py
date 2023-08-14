def replaceElements(arr):
    i = len(arr) - 1
    _max = -1
    while i > 0:
        curr = arr[i]
        arr[i] = _max
        _max = max(_max,curr)
        i+=1

