from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize variable to store the maximum water amount area
        # Initially set to 0 because there's no water in the container yet
        max_water_amount_area = 0

        # Loop through each element in the list height using index i
        for i in range(len(height)):
            # Loop through each element from i+1 to the end using index j
            for j in range(i + 1, len(height)):
                # Calculate the area between i and j
                # Area is determined by the distance (j - i) and the height of the shorter line
                area = (j - i) * min(height[i], height[j])

                # Update max_water_amount_area if the current area is larger
                max_water_amount_area = max(max_water_amount_area, area)

        # Return the maximum water amount area found
        return max_water_amount_area


# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solve = Solution().maxArea(height=height)
print(solve)  # Output should be 49
