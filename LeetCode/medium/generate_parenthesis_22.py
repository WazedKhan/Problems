class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        stack = []

        def backtrack(open_count, close_count):
            if close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result


res = Solution().generateParenthesis(n=3)
print(res)
