class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {"}": "{", "]": "[", ")": "("}
        for parentheses in s:

            if stack and parentheses in hash_map and hash_map[parentheses] == stack[-1]:
                # "parentheses in hash_map" make sure that we aren't working with opening parentheses66
                stack.pop()
            else:
                # if not closing parentheses then append the it into the stack
                stack.append(parentheses)

        if stack:
            return False
        return True
