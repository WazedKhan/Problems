class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for inx in range(len(nums)):
            if inx > 0 and nums[inx] == nums[inx - 1]:
                continue

            left, right = inx + 1, len(nums) - 1
            while left < right:
                three_sum = nums[inx] + nums[left] + nums[right]
                temp = [nums[inx], nums[left], nums[right]]
                if three_sum == 0:
                    res.append(temp)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res
