from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for index, value in enumerate(nums):
            requires = target - value
            if requires in visited:
                _min = min(index, visited[requires])
                _max = max(index, visited[requires])
                return [_min, _max]

            visited[value] = index

        return None

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for val in strs:
            sorted_val = "".join(sorted(val))

            if sorted_val in hash_map:
                hash_map[sorted_val].append(val)
            else:
                hash_map[sorted_val] = [val]

        return list(hash_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution().groupAnagrams(strs=strs)
print("sol: ", sol)
