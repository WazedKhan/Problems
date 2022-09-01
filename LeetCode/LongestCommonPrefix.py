
def longestCommonPrefix(strs):
    prefix = ''
    for char in range(len(strs[0])):
        for s in strs:
            if len(s) == char or s[char] != strs[0][char]:
                return prefix
        prefix += strs[0][char]

    return prefix

print(longestCommonPrefix(strs=["flower","flow","flight"]))