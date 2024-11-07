class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        if len(s) <= 2:
            return s
        for char in s:
            if len(stack) < 2:
                stack.append(char)
                continue
            if char != stack[-1] or char != stack[-2]:
                stack.append(char)
        return "".join(stack)
