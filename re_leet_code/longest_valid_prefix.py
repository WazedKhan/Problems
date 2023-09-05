def longestCommonPrefix(strs: list[str]):
    prefix = ""
    for index in range(len(strs[0])):
        for word in strs:
            if len(word) == index or strs[0][index] != word[index]:
                return prefix
        prefix += strs[0][index]
    return prefix


print(longestCommonPrefix(strs=["flower", "flow", "flight"]))
