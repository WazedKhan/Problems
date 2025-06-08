# Reinforcement Session 01: 08-06-2025
import heapq
from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1

        sorted_frequent = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)[:k]
        return [item[0] for item in sorted_frequent]

    def topKFrequentHeapQ(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item[0] for item in heapq.nlargest(k, count.items(), key=lambda item: item[1])]

    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
top_k = Solution().topKFrequent(nums=nums, k=k)
print(f"Result - Top K frequent: {top_k}")  # Output should be [1, 2] or similar based on the implementation

print(f"Result - Top K frequent HeapQ: {Solution().topKFrequentHeapQ(nums=nums, k=k)}")

print(f"Result - Top K frequent Bucket: {Solution().topKFrequentBucket(nums=nums, k=k)}")
