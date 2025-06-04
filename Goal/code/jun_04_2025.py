#User function Template for python3
class Solution:
    # Function to find the maximum sum of a subarray of size k
    def maximumSumSubarrayBruteForce(self,arr,k):
        max_sum = 0
        for i in range(0, len(arr)-k+1):
            max_sum = max(max_sum, sum(arr[i: i+k]))
        return max_sum

    def maximumSumSubarray(self,arr,k):
        current_sum = sum(arr[:k])
        max_sum = current_sum
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum

arr = [100, 200, 300, 400]
k = 2
solution = Solution().maximumSumSubarray(arr, k)
print("Maximum sum of subarray of size", k, "is:", solution)