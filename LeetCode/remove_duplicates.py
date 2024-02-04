def remove_duplicates(nums):
    nums_set = list(set(nums))
    k = 1
    for i in range(len(nums_set)):
        if nums[i] != nums_set[i]:
            nums[i] = nums_set
            k += 1
    return k


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(type(remove_duplicates(nums)))
