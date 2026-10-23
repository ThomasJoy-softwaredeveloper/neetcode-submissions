class Solution:
    def isValid(self, s: str) -> bool:
        closetoOpen = { ']':'[', ')':'(', '}':'{'} # hashMap
        stack = []
        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack