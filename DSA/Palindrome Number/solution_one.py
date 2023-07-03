# solution: 01:


def is_palindrome_01(number):
    str_number = str(number)
    return str_number == str_number[::-1]

# solution: 02:
def is_palindrome_02(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x = x // 10
    return x == half or x == half // 10


number = 121
print(is_palindrome_01(number))
print(is_palindrome_02(number))
