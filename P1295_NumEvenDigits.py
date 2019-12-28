#Problem
#Given a list of numbers, return the amount of numbers that have an even number of digits

#Solution
#For each number in the list...
#Initialize isEven=False
#If the number is less than 10, it has 1 digit, so isEven stays False
#If the number is greater than 10, we will floor divide it, and change isEven to True
#Once we get to a number less than 0, we can no longer floor divide it.
#Each time we floor divide, we switch the value of isEven

def findNumbers(nums: int) -> int:
    """
    >>> findNumbers([12,345,2,6,7896])
    2
    >>> findNumbers([555,901,482,1771])
    1
    """
    numEvens=0
    for i in nums:
        evenDigits=False
        while i>10:
            i=i//10
            evenDigits=not evenDigits
        if evenDigits:
            numEvens+=1
    return numEvens