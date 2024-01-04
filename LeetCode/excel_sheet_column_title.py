import math


def convertToTitle(columnNumber):
    max_alphabet = 26
    if max_alphabet >= columnNumber:
        capital_start_point = 64
        return chr(capital_start_point + columnNumber)

    result = ""
    while columnNumber > 0:
        reminder = (columnNumber - 1) % 26
        result = chr(65 + reminder) + result
        columnNumber = (columnNumber - 1) // 26
    return result


number = 2147483647
excel_column = convertToTitle(number)
print(f"The Excel column representation of {number} is: {excel_column}")


# print(convertToTitle(2147483647))
