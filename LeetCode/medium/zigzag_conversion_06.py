class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]

        temp_count = 0
        for i in s:
            for ar in arr:
                ar.append


s = "PAYPALISHIRING"
numRows = 3

result = Solution().convert(s, numRows)
print(f"Result: {result}")