def lengthOfLastWord(s):
    return list(map(str, s.rstrip().split()))[-1]


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))