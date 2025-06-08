# source: https://www.geeksforgeeks.org/python-sorted-function/

# sorted function takes any iterables e.g: list, string, tuples, dicts and returns a new sorted list
# sorted function keeps original iterable untouched, nums = [2, 3, 1] will unchanged while new list will be returned 1, 2, 3

a = [4, 1, 3, 2]
b = sorted(a)
print(f"original a: {a}")
print(f"sorted a as b: {b}")

# syntax or sorted: sorted(iterable, key=None, reverse=False)
# Parameters:
# iterable: The sequence to be sorted. This can be a list, tuple, set, string, or any other iterable.
# key (Optional): A function to execute for deciding the order of elements. By default it is None
# reverse (Optional): If True, sorts in descending order. Defaults value is False (ascending order)

# reverse=True helps sorted to arrange the elements
# from largest to smallest elements
b_descending_order = sorted(a, reverse=True)
print("a sorted in descending order: ", b_descending_order)

# sorting using key parameter
# lets sort list of string based on their len with key parameter
a = ["apple", "banana", "cherry", "date"]
res = sorted(a, key=len)
print(f"string sorted based on their len: {res}")

# Sorting a List of Dictionaries:
a = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 91},
    {"name": "Eve", "score": 78},
]

# sorting the dict a by score key
# with this sorted will return a new list where dict are sorted by score value
b = sorted(a, key=lambda x: x["score"], reverse=True)
print(f"list of dict sorted by score: {b}")

# -------------------------- Tasks -------------------------------------------

# 🔰 Level 1: Basics
# Sort a list of numbers
nums = [4, 2, 9, 1]
sorted_nums = sorted(nums)
print(f"sorted nums: {sorted_nums}")

# Sort a List of Strings Alphabetically
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print(f"sorted alphabetically {sorted_words}")

# Sort a Tuple Instead of List
tup = (3, 1, 5)
sorted_tup = sorted(tup)
print(f"sorted tup: {sorted_tup}")


# ⚙️ Level 2: Using key=
# Sort a List of Strings by Length
words = ["banana", "apple", "kiwi"]
word_sorted_len = sorted(words, key=len)
print(f"word sorted by len: {word_sorted_len}")

# Sort by Last Character
words = ["apple", "banana", "cherry"]
sorted_by_last_char = sorted(words, key=lambda x: x[-1])
print(f"word sorted by last char: {sorted_by_last_char}")

# Sort a List of Tuples by Second Element
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_by_snd_elem = sorted(pairs, key=lambda x: x[1])
print(f"sorted by second element: {sorted_by_snd_elem}")


# Sort a List of Strings by Number of Vowels
def count_vowels(word):
    return sum(1 for char in word.lower() if char in "aeiou")


words = ["apple", "banana", "cherry", "kiwi", "grape"]
sorted_by_vowels = sorted(words, key=count_vowels)
print(f"sorted by vowels: {sorted_by_vowels}")
