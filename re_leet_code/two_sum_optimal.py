# 1. Two Sum

# step 1: we declear a hash map to store index as value and key item as value
# step 2: iter over nums and check if target - current item == value
# step 3: check if value is in the hash map
# step 4: if not in hash map then store it in the hash map and move to next item of the list
# step 5: if value found in the hash map then take the index number and current index number return them as list

from typing import List

def twoSum(nums: List[int], target: int):
    hash_map = {}

    for index, value in enumerate(nums):
        target_value = target - value
        if target_value in hash_map:
            return [hash_map[target_value], index]
        else:
            hash_map[value]=index
    return
nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
