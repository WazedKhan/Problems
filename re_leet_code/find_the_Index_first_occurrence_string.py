def strStr(haystack: str, needle: str):
    # step 1: check if needle's length is bigger then haystack
    # if bigger then return -1 as we know needle should be part of haystack
    if len(haystack) < len(needle):
        return -1
    # step 2: loop though len(haystack) number and take the value from haystack's loop's index to len of needle
    for i in range(len(haystack)):
        # step 3: check if haystack's index's to len of needle is the need
        # like we have haystack with sadbutsad so we assume the current index is 0 as loop goes 0 to len(haystack)
        # so from haystack 0 to len(needle) will be haystack[0:3](len(sad)==3) assuming needle is "sad"
        # now from haystack[0:3] we have sad and index was 0 so we return 0
        if haystack[i : i + len(needle)] == needle:
            return i
        # step 4: we need to check if from step 3(haystack[index:len(needle)]) we have a string that's
        # length is less then needle then we can say needle is not part of haystack so we return -1
        if len(haystack[i : i + len(needle)]) < len(needle):
            return -1
    # step 5: if none of the condition matched then by default we can say that needle is not part of haystack
    # so we return -1
    return -1


haystack = "leetcode"
needle = "codeo"
print(strStr(haystack, needle))
