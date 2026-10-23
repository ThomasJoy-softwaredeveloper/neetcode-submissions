class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if self.minStack and self.minStack[-1] == tmp:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
   

    def getMin(self) -> int:
        return self.minStack[-1]

