# Two Sum - 1
"""
[Problem]
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
-----------------------------------------------------------------------------------------------------------------------------

[Input Example 1]

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
-----------------------------------------------------------------------------------------------------------------------------

[Pseudocode]
Step-1: Take num[i] add with num[j+1]
Step-2: If num[i]+num[j+1] == target return i and j+1
"""

def twoSum(nums, target)->list[int]:
    """Returns positon of items which addition is targer"""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


print(twoSum(nums=[3,2,4], target = 6))
