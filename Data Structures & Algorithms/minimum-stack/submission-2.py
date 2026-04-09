class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.curr_min:
            self.curr_min.append(val)
        else:
            self.curr_min.append(min(val, self.curr_min[-1]))

    def pop(self) -> None:
        if self.curr_min and self.stack:
            self.curr_min.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()