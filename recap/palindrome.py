import time


class Solution:
    def is_palindrome_modulus(self, x: int) -> bool:
        reverse = 0
        temp = x
        while temp != 0:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10
        return reverse == x

    def is_palindrome_string(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]

    def is_palindrome_two_pointer(self, x: int) -> bool:
        str_x = str(x)
        x_len = len(str_x)
        right_pointer = 0
        left_pointer = x_len - 1

        for _ in range(x_len):
            if str_x[left_pointer] != str_x[right_pointer]:
                return False

            elif right_pointer == left_pointer:
                return True

            left_pointer -= 1
            right_pointer += 1
        return True

    def is_palindrome_mathematical(self, x: int) -> bool:
        pass


number = -121
# solution = Solution().is_palindrome_modulus(number)
# print(solution)

solution = Solution().is_palindrome_string(number)
print(solution)

solution = Solution().is_palindrome_two_pointer(number)
print(solution)
