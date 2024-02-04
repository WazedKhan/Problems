def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


nums = [3, 2, 2, 3]
val = 2

print(removeElement(nums, val))
print(nums)
