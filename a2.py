def findNumbers(nums):
    count = 0
    for i in nums:
        even = False
        num = i
        while num >= 10:
            num = num//10
            even = not even
        if even:
            count += 1
    return count

nums = [12,345,2,6,7896]
findNumbers(nums)
findNumbers([100000])


