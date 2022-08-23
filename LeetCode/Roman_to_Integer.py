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