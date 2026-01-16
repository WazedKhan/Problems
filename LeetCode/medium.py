from typing import List


class Solution:
    # https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field
    # 2975. Maximum Square Area by Removing Fences From a Field
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Add boundaries
        """
        This function calculates the maximum square area that can be formed by removing fences from a field of size m x n.

        Parameters:
        m (int): The width of the field
        n (int): The height of the field
        hFences (List[int]): A list of horizontal fence positions
        vFences (List[int]): A list of vertical fence positions

        Returns:
        int: The maximum square area that can be formed, or -1 if it is not possible
        """
        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])

        # possible horizontal distances
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])
        max_dist = 0
        # possible vertical distance
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in h_dist:
                    max_dist = max(d, max_dist)

        MOD = 10**9 + 7
        return -1 if max_dist == 0 else (max_dist * max_dist) % MOD
