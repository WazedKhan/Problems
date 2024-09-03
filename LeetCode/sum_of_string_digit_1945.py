# 1945. Sum of Digits of String After Convert
class Solution:
    def get_char_value(self, char: str) -> str:
        return str(ord(char) - 96)

    def getLucky(self, s: str, k: int) -> int:
        int_str = "".join(self.get_char_value(char) for char in s)
        while k > 0:
            int_str = str(sum(int(i) for i in int_str))
            k -= 1
        return int(int_str)
