# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
