def firstPalindrome(words):
    for i in words:
        if i == i[::-1]:
            return i
    return ''

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))