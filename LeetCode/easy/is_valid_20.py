class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i in p_map:
                if not stack:
                    return False
                elif stack[-1] == p_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0
