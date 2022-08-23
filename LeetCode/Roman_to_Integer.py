"""
[Pseudocode]
step-1: make dict to store key as symbola value as the value of symbols
step-2: take char from string
step-3: find the char value in dict
step-4: add and store value in var
"""

def romanToInt(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0

    for index, char in enumerate(s):
        if index+1 < len(s) and roman[char] < roman[s[index+1]]:
            value -= roman[char]
        else:
            value += roman[char]

    return value


romanToInt('MCMXCIV')