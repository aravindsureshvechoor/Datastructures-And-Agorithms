def ispalindrome(a):
    b = a[::-1]
    if a == b:
        return True
    return False
a="malayalam"


print(ispalindrome(a))
