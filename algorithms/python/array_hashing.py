import heapq
from collections import Counter
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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        sorted_encounter: dict = dict(
            sorted(
                counter.items(),
                key=lambda item: item[1],
                reverse=True,
            )[:k]
        )
        return list(sorted_encounter.keys())

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for key, value in freq_map.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for num in heap:
            res.append(num[1])
        return res


nums = [3, 0, 1, 0]
k = 1
sol = Solution().topKFrequentHeap(nums=nums, k=k)
print("topKFrequent: ", sol)
