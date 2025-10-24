from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows - 1):
            tem_row = [0] + result[-1] + [0]
            new_row = []
            for j in range(len(result[-1]) + 1):
                new_row.append(tem_row[j] + tem_row[j + 1])
            result.append(new_row)
        return result

    def generateCoefficients(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            coeffs = [1]

            for k in range(i):
                coeffs.append(coeffs[-1] * (i - k)//(k+1))
            result.append(coeffs)
        return result


numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
solution = Solution().generate(numRows)
print(solution)
