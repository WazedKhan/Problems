from collections import defaultdict


def checkIfPangram(sentence):
    hash_table = defaultdict(int)
    for char in sentence:
        hash_table[char] += 1

    return len(hash_table) == 26

sentence = "leetcode"
print(checkIfPangram(sentence))