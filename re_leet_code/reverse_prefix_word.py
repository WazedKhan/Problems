# 2000. Reverse Prefix of Word
def reverse_prefix(word: str, ch: str):
    prefix = ""
    ch_index: int = 0
    break_triggered: bool = False

    for index in range(len(word)):
        prefix += word[index]
        if word[index] == ch:
            ch_index = index
            break_triggered = True
            break
    if not break_triggered:
        return word
    reversed_prefix = prefix[::-1]
    word_without_prefix = word[ch_index + 1 :]
    return reversed_prefix + word_without_prefix


word = "xyxzxe"
ch = "z"
# Output: "dcbaefd"

print(reverse_prefix(word, ch))
print("zxyxxe" == reverse_prefix(word, ch))
