import heapq
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for char in strs:
            char_val = "".join(sorted(char))
            if char_val in hash_map:
                hash_map[char_val].append(char)
            else:
                hash_map[char_val] = [char]
        return list(hash_map.values())

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        heap_q = []

        for key, value in num_freq.items():
            heapq.heappush(heap_q, (value, key))

            if len(heap_q) > k:
                heapq.heappop(heap_q)

        return [item[1] for item in heap_q]


# strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
# sol = Solution().groupAnagrams(strs=strs)
nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution().topKFrequent(nums=nums, k=k)
print("sol: ", sol)
