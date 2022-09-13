def searchInsert(nums, target):
    low, high = 0, len(nums)
    last_pos = 0
    while high > low:
        mid = (low + high)//2
        if (target == nums[mid]):
            return mid
        elif (target > nums[mid]):
            low = mid + 1
        else:
            high = mid - 1

    if len(nums) - 1 >= low and nums[low] < target:
        return low+1
    else: return low

nums = [1,3,5,6]
target = 4

print(searchInsert(nums, target))