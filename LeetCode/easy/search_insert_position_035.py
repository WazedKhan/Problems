# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        This function takes a sorted list of integers and a target integer,
        and returns the index at which the target should be inserted to keep
        the list sorted. If the target is found in the list, it returns the index
        of the target.

        Steps:
        - Iterate over the nums list.
        - For each element, check if it is equal to the target. If true, return its index.
        - If the current element is less than the target and the next element is greater than or equal to the target,
          return the index of the next element.
        - If the target is greater than all elements, return the length of the list (insert at the end).
        :param nums: List[int] - A sorted list of integers.
        :param target: int - The target integer to search for.
        :return: int - The index at which the target should be inserted.

        Time Complexity: O(n) - where n is the length of the nums list.
        Space Complexity: O(1) - no extra space used.
        """
        if target <= nums[0]:
            return 0

        for index in range(len(nums)-1):
            if nums[index] == target:
                return index

            if nums[index] < target and nums[index+1] >= target:
                return index +1

        return len(nums)

    def searchInsert_binary_search(self, nums: List[int], target: int) -> int:
        """
        This function takes a sorted list of integers and a target integer,
        and returns the index at which the target should be inserted to keep
        the list sorted. If the target is found in the list, it returns the index
        of the target.

        Steps:
        - Initialize left and right pointers.
        - Perform binary search to find the correct insertion index.
        :param nums: List[int] - A sorted list of integers.
        :param target: int - The target integer to search for.
        :return: int - The index at which the target should be inserted.

        Time Complexity: O(log n) - where n is the length of the nums list.
        Space Complexity: O(1) - no extra space used.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left




# Example usage:
nums = [1, 3, 5, 6]
target = 5
solution = Solution()
print(solution.searchInsert(nums, target))  # Output: 2
# Example usage:
nums = [1, 3, 5, 6]
target = 2
solution = Solution()
print(solution.searchInsert(nums, target))  # Output: 1
# Example usage:
nums = [1, 3, 5, 6]
target = 7
solution = Solution()
print(solution.searchInsert(nums, target))  # Output: 4

        