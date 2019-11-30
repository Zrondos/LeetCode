#Problem: Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#Solution: Simply use Pythons .lower() method

def toLowerCase(str: str) -> str:
    return str.lower()
def check_answer():
    return 'hello' == toLowerCase("Hello")
print(check_answer())