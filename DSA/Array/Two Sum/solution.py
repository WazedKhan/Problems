def twoSum(nums, target):
    for current_index in range(len(nums)):
        # get first index as current value 
        for next_index in range(current_index+1, len(nums)):
            # current_index + 1 will make sure that we are not taking same index
            if nums[current_index]+nums[next_index] == target:
                #checks if current index and next_index addition is same as target  
                return [current_index, next_index]


nums = [3,3]
target = 6
print(twoSum(nums, target))