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


solution = Solution()
numbers = [2, 3, 4]
target = 6

print("Two Sum ll Result:", solution.twoSum(numbers, target))
