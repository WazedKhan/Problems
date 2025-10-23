class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            result = ""
            for index in range(len(s)-1):
                sum = (int(s[index]) + int(s[index+1])) % 10
                result += str(sum)

            s = result
        return s[0] == s[1]
