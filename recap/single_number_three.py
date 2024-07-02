from typing import List

# step 1: first will store count of every number in a hash map
# step 2: check if any of the value in the hash map is 1 then we store it in array
# step 3: return the array


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = []
        # declare the the has map
        hash_map = {}
        for i in range(len(nums)):
            # check for every item and store their count in the hash map
            # here key is the element of the array and value is their count/frequency
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        # check if any value in the hash map is 1
        for key, value in hash_map.items():
            # if value is 1 then we have find the item which suppose to appear onces
            if value == 1:
                result.append(key)
        return result


nums = [1, 2, 1, 3, 2, 5]  # output: [3,5]
solution = Solution().singleNumber(nums=nums)
print(solution)
