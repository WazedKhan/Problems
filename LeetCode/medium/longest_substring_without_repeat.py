class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_map = {}
        max_len = 0
        win_start = 0

        for idx, value in enumerate(s):
            last_index = seen_map.get(value)
            if last_index is not None and last_index >= win_start:
                win_start = last_index + 1

            seen_map[value] = idx

            max_len = max(max_len, idx - win_start + 1)

        return max_len
