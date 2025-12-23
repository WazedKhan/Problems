# User function Template for python3
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

    def frequencySort(self, s: str) -> str:
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        sorted_chars = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        res = ""
        for item in sorted_chars:
            res += item[0] * item[1]

        return res


char = "tree"
solution = Solution().frequencySort(s=char)
print("Res: ", solution)
