class MinStack:

    def __init__(self):
        self.array = []
        self.helper = []

    def push(self, val: int) -> None:
        self.array.append(val)
        val = min(val, self.helper[-1] if self.helper else val)
        self.helper.append(val)
    def pop(self) -> None:
        self.array.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.helper[-1]
        
