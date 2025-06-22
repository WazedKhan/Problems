from collections import deque
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointer approach:
        - Start with two pointers at the beginning and end of the sorted list.
        - Move the pointers based on the sum comparison with the target.
        - Return the 1-based indices when the correct pair is found.
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]

    def maxSlidingWindowB(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            res.append(max(nums[i : i + k]))
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for idx, val in enumerate(nums):
            if dq and dq[0] <= idx - k:
                dq.popleft()

            while dq and nums[dq[-1]] < val:
                dq.pop()

            dq.append(idx)

            if idx >= k - 1:
                res.append(nums[dq[0]])

        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

solution = Solution().maxSlidingWindow(nums, k)
print(solution)  # Output: [3, 3, 5, 5, 6, 7]
