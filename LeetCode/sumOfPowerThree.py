def isPowerOfThree(n):
    pThree = 3
    hightest = 0
    while pThree <= n:
        hightest += 1
        pThree *= 3
    return hightest

def checkPowersOfThree(n):
    check_value, value, powers = n, 0, []
    while n > 0:
        squire = isPowerOfThree(n)
        if squire not in powers:
            value += (3**squire)
            print('n= ',n, 'squire= 3^',squire, 'value= ', value)
            powers.append(squire)
            n -= 3**squire
        else:
            n -= 3**squire
            continue
    return value == check_value


print(checkPowersOfThree(91))