# we will get the first item and considering it we will apply two sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need to return result as list of lists
        results = []
        nums.sort()
        for index, value in enumerate(nums):
            # lets avoid using same value twice
            if index > 0 and value == nums[index - 1]:
                continue

            # so now we can get next two pointer value to get three sum
            left_pointer, right_pointer = index + 1, len(nums) - 1
            # we need keep moving pointer to get value 0
            while left_pointer < right_pointer:
                three_sum = value + nums[left_pointer] + nums[right_pointer]
                # update pointer position depending on the three_sum value
                if three_sum > 0:
                    right_pointer -= 1
                elif three_sum < 0:
                    left_pointer += 1
                else:
                    results.append([value, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    # if next left pointer is same as previous left pointer then we need to skip it
                    # as we dont want duplicates
                    while (
                        nums[left_pointer] == nums[left_pointer - 1]
                        and left_pointer < right_pointer
                    ):
                        left_pointer += 1
        return results


nums = [-1, 0, 1, 2, -1, -4]  # Output: [[-1,-1,2],[-1,0,1]]
results = Solution().threeSum(nums)
print(f"Result: {results}")
