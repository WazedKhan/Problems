class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracer = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        val = min(value, self.min_tracer[-1] if self.min_tracer else value)
        self.min_tracer.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_tracer.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracer[-1]
