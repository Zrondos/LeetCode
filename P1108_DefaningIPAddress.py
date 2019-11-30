###
#Problem: Given a valid (IPv4) IP address, 
# return a defanged version of that IP address. 
# A defanged IP address replaces every period "." with "[.]".
#Solution: For loop through the string, use if statement to change . -> [.] 
# then add to new_string

def defangIPaddr(address: str) -> str:
    """
    >>> defangIPaddr("1.1.1.1")
    '1[.]1[.]1[.]1'
    >>> defangIPaddr("255.100.50.0")
    '255[.]100[.]50[.]0'
    """
    new_string=""
    for i in address:
        if i==".":
            to_append="[.]"
        else:
            to_append=i
        new_string+=to_append    
    return new_string