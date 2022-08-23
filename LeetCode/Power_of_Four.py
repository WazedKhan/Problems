# https://leetcode.com/problems/power-of-four/
import math

def isPowerOfFour(n: int) -> bool:
    try:
        return str(math.log(n, 4)).split(".")[1] == '0'
    except ValueError:
        return False

print(isPowerOfFour(-2147483648))


