def twoSum(nums, target):
    for key, value in enumerate(nums):
        current_value = value
        for value in range(key+1, len(nums)):
            result = nums[value]+current_value
            if result == target:
                return key, value


nums = [3,3]
target = 6
print(twoSum(nums, target))