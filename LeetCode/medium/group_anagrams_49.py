from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        for item in strs:
            key = "".join(sorted(item))
            hash_map.setdefault(key, []).append(item)

        return list(hash_map.values())
