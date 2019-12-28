#Problem
#Remove vowels from a string (S)

#Solution
#If the first letter is vowel, remove S[0] from S
#Elif S[i] is a vowel, change S to everything up to but not including S[i] + S[i+1] until the end of the string
#Else, S[i] is not a vowel, and we can move onto the next character in the string

def removeVowels(S: str) -> str:
    """
    >>> removeVowels('leetcodeisacommunityforcoders')
    'ltcdscmmntyfrcdrs'

    >>> removeVowels('aeiou')
    ''
    """
    vowels=['a','e','i','o','u']
    i=0
    while i<len(S):
        if S[0] in vowels:
            S=S[1:]
        elif S[i] in vowels:
            S=S[:i]+S[i+1:]
        else:
            i+=1
    return S