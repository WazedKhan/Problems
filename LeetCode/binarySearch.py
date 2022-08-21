# LeetCode - 704. Binary Search (Easy)

"""
Problem:
A target is given we need to find the index number of the target from a given ascending ordered array.

"""

"""
Input and Output Example:
(1)/
nums = [-1, 4, 6, 7]
target = 6
output = 2

(2)//
nums = [1]
target = 7
output = -1
"""

"""
Pseudocode:

1: Set high and low to len(array), 0
2: Check if mid (low+high // 2) is targer0
3: If targer is greater than mid then set low = next index number (mid + 1) of mid as mid was checked
4: If target is less than mid then set high = preivous index number of mid(mid - 1) as high as mid was chacked
5: Keep repeating steps until low <= high
6: Cant find target in array return -1
"""

def binarySearch(array, target):
    low, high = 0, len(array)-1
    while low <= high:
        mid = (high + low) // 2
        curr_val = array[mid]
        if curr_val == target:
            return mid
        elif curr_val > target:
            high = mid - 1
        elif curr_val < target:
            low = mid + 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9
length = len(nums)

binarySearch(array= nums,target=target)


# Passed all test case in LeetCode