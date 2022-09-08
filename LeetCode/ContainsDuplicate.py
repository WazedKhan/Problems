from collections import defaultdict
nums = [1,2,3,4]

def containsDuplicate(nums):
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    # return False
    
    counter = defaultdict(int)
    for i in nums:
        if i in counter:
            return True
        if i not in counter:
            counter[i] += 1
    return False

    # for key, value in counter.items():
    #     if value > 1:
    #         return True
    # return False

print(containsDuplicate(nums))