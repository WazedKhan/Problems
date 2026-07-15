import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
        stack = []

        for token in tokens:
            if token in ops:
                num_1 = stack.pop()
                num_2 = stack.pop()
                operation = ops[token]
                res = operation(int(num_2), int(num_1))
                stack.append(res)
            else:
                stack.append(token)

        return int(stack[0])
        # NOTE: we could append token as int() then we wouldn't need to convert it before return or operation
