def plusOne(digits):
    num = ''
    for i in digits:
        num += str(i)
    num = str(int(num)+1)
    return [n for n in num]

digits = [1,2,3]

print(plusOne(digits))