roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

n = 58
value = ''

for i in roman:
    if n//i:
        value += (n//i)*roman[i]
    n = int(n%i)
print(value)