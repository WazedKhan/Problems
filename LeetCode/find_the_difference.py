from collections import Counter

def findTheDifference(s, t):
    cs = Counter(s)
    ct = Counter(t)
    print(ct)
    for key, value in ct.items():
        if key not in cs or value != cs[key]:
            return key

s = "abcd"
t = "abcde"

print(findTheDifference(s, t))