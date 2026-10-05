class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dup = nums.copy()
        dup.sort()
        print(dup.sort())
        print(nums)


sol = Solution().containsDuplicate([1, 2, 3, 1])
