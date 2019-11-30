#Problem
#You're given strings J representing the types of stones that are jewels, 
# and S representing the stones you have.  
# Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.
#The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

#Solution
#Convert string J into array using for loop.
#For loop through S and check if each letter is a member of the J_array. If so, add 1 to solution
def numJewelsInStones(J: str, S: str) -> int:
    """
    >>> numJewelsInStones("aA","aAAbbbb")
    3
    >>> numJewelsInStones("z","ZZ")
    0
    """
    jewels_array=[]
    for i in J:
        jewels_array+=i
    num_of_jewels=0
    for i in S:
        if i in jewels_array:
            num_of_jewels+=1
    return num_of_jewels

        