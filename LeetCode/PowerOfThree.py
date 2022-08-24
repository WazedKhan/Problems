import math
def isPowerOfThree(n):
    if n == 1:
        return True
    pThree = 3
    while pThree <= n:
        if pThree == n:
            return True
        pThree *= 3
    return False



print(isPowerOfThree(45))
