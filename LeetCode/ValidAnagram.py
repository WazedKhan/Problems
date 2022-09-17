def isAnagram(n, t):
    for i in t:
        if i not in n:
            return False
        else:
            n = n.replace(i, '', 1)
    return len(n) <= 0, n


s = 'ab'
t = 'as'

print(isAnagram(s, t))