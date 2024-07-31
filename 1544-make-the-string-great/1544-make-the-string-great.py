class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if i.islower() and stack[-1].isupper() and i.upper() == stack[-1].upper():
                    stack.pop()
                elif i.isupper() and stack[-1].islower() and i.upper() == stack[-1].upper():
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        return "".join(stack)
        