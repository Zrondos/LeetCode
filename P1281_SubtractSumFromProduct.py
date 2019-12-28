#Problem
#Given a number n, return ProductOfDigits-sumOfDigits
#n is always greater than or equal to 1

#Solution
#Start with the sum being 0, and the product being 1 (Because n will always be greater than 1, we don't have to worry about a single digit 0)
#Take the last digit, add to sumOfDigits and multiply by ProductOfDigits
#Remove the last digit of n until there are no more digits left
#Return ProductOfDigits-sumOfDigits

def subtractProductAndSum(n: int) -> int:
    """
    >>> subtractProductAndSum()
    """
    productDigits=1
    sumDigits=0
    while n>0:
        lastDigit=n%10
        productDigits*=lastDigit
        sumDigits+=lastDigit
        n=n//10
    return productDigits-sumDigits