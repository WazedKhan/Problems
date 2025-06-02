from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given:
            - strs: List of strings
        Returns:
            - A list of grouped anagrams

        Problem:
            - Group all the anagrams together from the input list of words.

        Thought Process:
            - Anagrams, when sorted, result in the same string.
            - Use the sorted version of each word as a key in a hash_map.
            - Group words that share the same sorted string.

        Approach:
            - Sort each word to get its anagram base form.
            - Use a hash_map to collect words with the same base.

        Solution:
            - For each word, sort it and use the result as a key.
            - Append the original word to the list at that key.
            - Return all grouped values as the result.
        """
        hash_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]

        return list(hash_map.values())

    def groupAnagramsOptimized(self, strs: List[str]):
        """
        Given:
            - strs: List of strings
        Returns:
            - A list of grouped anagrams

        Problem:
            - Same as above: group all anagrams together from the input list.

        Thought Process:
            - Instead of sorting, represent a word by the frequency of each character (since all inputs are lowercase a–z).
            - Count characters using a fixed-size list (length 26) where index 0 represents 'a' and 25 represents 'z'.
            - Tuples of counts can serve as unique keys in a hash_map.

        Approach:
            - For each word, count the frequency of each letter.
            - Use the tuple of counts as a key to group words.

        Solution:
            - Initialize an empty defaultdict of lists.
            - For each word, compute its character count array and convert it to a tuple.
            - Append the word to the hash_map at that tuple key.
            - Return all grouped values.
        """
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())


# Example usage:
solution = Solution()
input = ["eat"]
print(solution.groupAnagrams(input))
print("Optimized version:")
solution.groupAnagramsOptimized(input)
