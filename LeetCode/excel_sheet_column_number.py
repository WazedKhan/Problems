def titleToNumber(columnTitle):
    res = 0
    for i in columnTitle:
        res += (ord(i)-64)
    return res

print(titleToNumber("AA"))