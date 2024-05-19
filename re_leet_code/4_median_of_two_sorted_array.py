from typing import List


def find_median(nums: List[int]) -> float:
    # find the middle number if num:array contains odd numbers
    nums_len: int = len(nums)
    # to find median array must have to be sorted
    nums = sorted(nums)

    if nums_len % 2 == 1:
        return float(nums[nums_len // 2])
    else:
        right = nums_len // 2
        left = nums_len // 2 - 1
        return (nums[right] + nums[left]) / 2


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = list(set(nums1)) + list(set(nums2))
    return find_median(nums)


nums_1 = [1, 2, 4]
nums_2 = [3]
print(findMedianSortedArrays(nums_1, nums_2))
