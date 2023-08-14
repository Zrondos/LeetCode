def duplicateZeros(arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        #Starting left to right, if there is a zero, shift all following elements to the right by 1, then insert 0
        length = len(arr)
        index = 0
        while index < length - 1:
            if arr[index] == 0:
                last = length - 1
                while last > index:
                     arr[last] = arr[last - 1]
                     last -= 1
                arr[index+1] = 0
                index += 1
            index += 1
        if (index < length - 1) and arr[index] == 0:
            arr[index+1] = 0
        return arr
arr = [1,0,2,3,0,4,5,0]
arr = [0,0,0,0,0,0,0]
duplicateZeros(arr)
print(arr)

        