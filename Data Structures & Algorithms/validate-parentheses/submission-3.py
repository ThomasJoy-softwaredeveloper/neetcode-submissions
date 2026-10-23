class Solution:
    def isValid(self, s: str) -> bool:
        closetoOpen = { ']':'[', ')':'(', '}':'{'}
        stack = []
        for c in s:
            if c in closetoOpen and not stack:
                return False
            elif c in closetoOpen and stack[-1] == closetoOpen[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack