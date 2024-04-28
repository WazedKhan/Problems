# step 1:


def strStr(haystack: str, needle: str):
    # step 1: check if needle's length is bigger then
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        if haystack[i : i + len(needle)] == needle:
            return i
        if len(haystack[i : i + len(needle)]) < len(needle):
            return -1
    return -1


haystack = "leetcode"
needle = "codeo"
print(strStr(haystack, needle))
