def removeDuplicates(nums):
    if not nums:
        return 0
    
    current_unique_index = 0
    for index in range(1, len(nums)):
        if nums[current_unique_index] != nums[index]:
            current_unique_index += 1
            nums[current_unique_index] = nums[index]
    return current_unique_index + 1

# Example usage: misleading
nums = [1, 2, 2, 3]
k = removeDuplicates(nums)
print(f"The number of unique elements is {k}. The array is now: {nums[:k]}")
