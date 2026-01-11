class Solution:
    def pushZerosToEnd(self, arr, n):
        count = 0
        for i in arr:
            if i != 0:
                arr[count] = i
                count += 1
        while count < n:
            arr[count] = 0
            count += 1
        return arr


arr = [3, 5, 0, 0, 4]
n = 5
print(Solution().pushZerosToEnd(arr=arr, n=n))
