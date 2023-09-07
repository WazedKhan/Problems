symbol_value = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    result = 0
    for index, numeral in enumerate(s):
        if symbol_value[numeral] < symbol_value[s[index + 1]]:
            result -= symbol_value[numeral]
        else:
            result += symbol_value[numeral]
    return int(result)


print(romanToInt("MCMXCIV"))
