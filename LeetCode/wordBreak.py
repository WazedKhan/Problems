def wordBreak(s, wordDict):
    for i in wordDict:
        if i in s:
            print("yes")
        else:
            print("no")
    return s


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat", "okay"]

print(wordBreak(s, wordDict))
