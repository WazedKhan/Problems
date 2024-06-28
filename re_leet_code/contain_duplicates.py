from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        return len(set(nums)) != len(nums)
        # solution 2
        hash_set = set()
        for number in nums:
            if number in hash_set:
                return True
            hash_set.add(number)
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

solution = Solution().containsDuplicate(nums)
print(solution)
