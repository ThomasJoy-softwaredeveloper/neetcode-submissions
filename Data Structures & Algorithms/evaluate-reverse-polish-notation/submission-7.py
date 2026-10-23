from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for c in tokens:
            try:
                num = int(c)  # Attempt to convert to integer
                stack.append(num)
            except ValueError:
                if c in operators and len(stack) >= 2:
                    m = stack.pop()
                    n = stack.pop()
                    if c == '+':
                        result = n + m
                    elif c == '-':
                        result = n - m
                    elif c == '*':
                        result = n * m
                    elif c == '/':
                        result = int(n / m)  # Integer division as required
                    stack.append(result)
        
        return stack[-1]
