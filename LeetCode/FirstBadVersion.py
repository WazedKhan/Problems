from turtle import right


def isBadVersion(n):
    if n >= 4:
        return True
    else: return False


def firstBadVersion(n = 5):
    low, high = 1, n
    while high>low:
        mid = low+(high-low)//2
        if isBadVersion(mid):
            high = mid
        else: low = mid+1
    return low


print(firstBadVersion())