from collections import Counter, deque
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

    def checkInclusionBrute(self, s1: str, s2: str) -> bool:
        """
        first count the frequency of s1
        then take the window len(s1) and count frequency of that
        and compare it with frequency of s1
        """
        s1_freq_count = Counter(s1)
        window_size = len(s1) - 1

        for idx in range(len(s2) - window_size):
            curr_window = s2[idx : idx + window_size + 1]
            curr_win_f_count = Counter(curr_window)

            if curr_win_f_count == s1_freq_count:
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_count = Counter(s2[: len(s1)])
        # lets compare first widow if that match
        if s1_count == window_count:
            return True

        # now for per iteration remove the left item from window count
        # and add i value in window count
        # we must start our iteration from len(s1) as we already taken first window
        for idx in range(len(s1), len(s2)):
            left_char = s2[idx - len(s1)]
            window_count[left_char] -= 1
            if window_count.get(left_char) == 0:
                del window_count[left_char]

            window_count[s2[idx]] += 1

            if window_count == s1_count:
                return True

        return False


s1 = "adc"
s2 = "dcda"

solution = Solution().checkInclusion(s1, s2)
print(solution)  # Output: [3, 3, 5, 5, 6, 7]
