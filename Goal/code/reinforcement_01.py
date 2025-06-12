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

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for freq, num in heap:
            result.append(num)
        return result

    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)

        sorted_tuple = sorted(freq_map.items(), key=lambda items: items[1], reverse=True)
        res = ""
        for item in sorted_tuple:
            res += item[0] * item[1]

        return res

    def frequencySortBucket(self, s: str) -> str:
        freq_map = Counter(s)

        bucket = [[] for _ in range(len(s) + 1)]

        for char, freq in freq_map.items():
            bucket[freq].append(char)

        res = []
        for bucket_id in range(len(bucket) - 1, 0, -1):
            for item in bucket[bucket_id]:
                res.append(item * bucket_id)

        return "".join(res)

    def frequencySortLexicalTie(self, s: str) -> str:
        freq_map = Counter(s)

        sorted_items = sorted(freq_map.items(), key=lambda item: (-item[1], item[0]))

        res = []
        for item in sorted_items:
            res.append(item[0] * item[1])

        return "".join(res)
