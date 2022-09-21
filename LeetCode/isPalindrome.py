s = "0P"

def isPalindrom(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    for i in s:
        if i not in alphabets and i not in alphabets.upper() and i not in nums:
            s = s.replace(i, '')
    if s.lower() == s.lower()[::-1]:
        return True

    return False

print(isPalindrom(s))