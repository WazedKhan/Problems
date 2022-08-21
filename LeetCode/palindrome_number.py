# LeetCode Palindrome Number - 9

"""                 Pseudocode

1: First convert int into string
2: Reverse the string
3: try to covert the string into int and store in a var if valueError return False
4: if reversed is == given int return True
5: return False
"""

def isPalindrome(x):
    x = str(x)

    rev = x[::-1]

    try:
        rev = int(rev)
    except ValueError:
        return False

    if rev == int(x):
        return True
    return False

print(isPalindrome(153))