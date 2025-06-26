# prime number is only divisible by 1 and that number itself
# prime number is greater then 1

import math


def is_prime(number: int):
    """Brute force"""
    # if number is 1 or less then 1 then its not a prime number
    if number <= 1:
        return False

    # iter every item which starts from 2 and ends before number:
    limit = int(math.sqrt(number + 1))
    for value in range(2, limit):
        # if number is divisible by value: which is number less then the number
        # then its not prime number as prime number can't be divided by any other number itself
        print("dude!")
        if number % value == 0:
            return False

    if limit <= 2 and number % limit == 0:
        return False

    return True


number = 3
print(f"Number {number} is prime: {is_prime(number)}")
