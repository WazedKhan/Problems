from typing import List

# step 1: first will store count of every number in a hash map
# step 2: check if any of the value in the hash map is 1, if so return the key


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # declare the the has map
        hash_map = {}
        for i in range(len(nums)):
            # check for every item and store their count in the hash map
            # here key is the element of the array and value is their count/frequency
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        # check if any value in the hash map is 1
        for key, value in hash_map.items():
            # if value is 1 then we have our result then we dont need to iter anymore we can return the value
            if value == 1:
                return key
        # as its promised that there will be single item/element in the array we dont need to return anything
        # so we can just leave it or we can return empty value
        return


nums = [2, 2, 1]  # output: 1
solution = Solution().singleNumber(nums=nums)
print(solution)
