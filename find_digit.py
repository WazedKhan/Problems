# https://www.hackerrank.com/challenges/find-digits

from functools import cache


def findDigits(n):
    digit = int(n)
    count = 0
    for i in n:
        try:
            if digit%int(i) == 0:
                count += 1
        except:
            continue
    return count

t = int(input().strip())

for t_itr in range(t):
    n = input().strip()
    print(findDigits(n))