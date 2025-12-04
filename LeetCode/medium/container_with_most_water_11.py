# LeetCode 11. Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Pseudocode:
        The problem is we dont know the max area where we we can store most of the water
        So we can store from the start to end of the container but if the starting height of container is 1 then
        max we can store height of 1 as more then that will spile the water regardless the end height
        so if len is 9 and height is 1 then container can contain Area = length × width

        So, what we can do it use two pointer solution to find the max area
        - initialize two pointer left and right, left with value of index 0 and
          right index len(arr)-1 and res which contain most largest value
        - we will continue until our left and right point cross their path
        - we will be moving our smallest pointer as we know smallest length contain less water
        - each time we will check which one is largest previous area which stored in res
        - at the end we return the res as res will be containing the largest area value we got
        """
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
