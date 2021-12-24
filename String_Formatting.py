def DecimalOctal(num, divisor):
    octal = ''
    while (num != 0):
        octal += str(num % divisor)
        num = int(num / divisor)
    print((octal)[::-1])
    

DecimalOctal(127, 2)