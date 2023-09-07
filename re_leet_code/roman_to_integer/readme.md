# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

We need to scan from left to right, subtracting the left value from the right value when the left value is smaller. Otherwise, we add the left value to the right value, store the result in a variable, and then return it.

# Approach

<!-- Describe your approach to solving the problem. -->

1. First, we create a hashmap `symbol_value` to store the numerical value for the Roman symbol
2. Take a variable `result` with value 0
3. scan/loop through each item then take the `index` and `numeral(char)` of each item in the string
4. check if left value `symbol_value[numeral]` is less then right next value `symbol_value[s[index + 1]]`
5. In step (4) put and condition to check if the next right value is out of index `symbol_value[s[index + 1]]` to make sure that the array is not out of index
6. if the condition is true then subtract the left value from the right value `result -= symbol_value[numeral]`
7. eles add left value with right value `result += symbol_value[numeral]`

# Complexity

-   Time complexity:
    <!-- Add your time complexity here, e.g. $$O(n)$$ -->

        $$O(n)$$

-   Space complexity:
    <!-- Add your space complexity here, e.g. $$O(n)$$ -->
        $$O(1)$$

# Code

```
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for index, numeral in enumerate(s):
            if index + 1 < len(s) and symbol_value[numeral] < symbol_value[s[index + 1]]:
                result -= symbol_value[numeral]
            else:
                result += symbol_value[numeral]
        return int(result)
```
