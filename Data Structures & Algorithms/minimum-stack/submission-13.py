class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        # val = min(val,self.minStack[-1] if self.minStack else val)
        # self.minStack.append(val)
        # if self.minStack and val <= self.minStack[-1]:
        #     self.minStack.append(val)
        # elif not self.minStack:
        #     self.minStack.append(val)
            

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack: 
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None