class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.stack) if len(self.stack) > 0 else 0

    def pop(self) -> None:
        self.stack.pop()
        self.minVal = min(self.stack) if len(self.stack) > 0 else 0

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
