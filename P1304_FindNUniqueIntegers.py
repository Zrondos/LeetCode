#Problem
#Given an integer n>=1, return an array with that many elements, that's sum adds to zero

#Solution
#Whenever 2 numbers need to be added, we can add them in the pair [x,-x]
#If only 1 number needs to be added, we can add [0]
#If n is odd, we add n//2 pairs, and [0]
#If n id even, we add n//2 pairs


def sumZero(n: int):
    """
    >>> sumZero(5)
    [0, 2, -2, 1, -1]

    >>> sumZero(1)
    [0]

    >>> sumZero(3)
    [0, 1, -1]

    """
    if n%2==0:
        new_array=[]
    else:
        new_array=[0]
    num_elems_to_add=n//2
    while num_elems_to_add>=1:
        new_array.extend([num_elems_to_add,-num_elems_to_add])
        num_elems_to_add-=1
    return new_array