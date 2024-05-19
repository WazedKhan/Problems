def removeDuplicates(nums):
    if not nums:
        return 0
    
    next_unique_index = 0
    for index in range(1, len(nums)):
        if nums[next_unique_index] != nums[index]:
            next_unique_index += 1
            nums[next_unique_index] = nums[index]
    return next_unique_index + 1

# Example usage:
nums = [1, 1, 2]
k = removeDuplicates(nums)
print(f"The number of unique elements is {k}. The array is now: {nums[:k]}")
