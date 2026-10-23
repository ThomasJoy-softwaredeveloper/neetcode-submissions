class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
# Instantiate the MinStack class
minStack = MinStack()

# Push elements onto the stack
minStack.push(1)
minStack.push(2)
minStack.push(0)

# Get the minimum element
print(minStack.getMin())  # Output: 0

# Pop the top element
minStack.pop()

# Get the top element
print(minStack.top())  # Output: 2

# Get the minimum element
print(minStack.getMin())  # Output: 1