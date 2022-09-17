def isAnagram(s, t):
    if len(s) != len(t):
        return False

    hash_s = {}
    hash_t = {}
    for i in range(len(t)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    for i in hash_s:
        if hash_s[i] != hash_t.get(i):
            return False

    return True

s = 'cat'
t = 'rat'

print(isAnagram(s, t))