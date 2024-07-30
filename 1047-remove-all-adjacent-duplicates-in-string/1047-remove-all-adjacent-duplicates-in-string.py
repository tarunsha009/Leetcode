class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) < 1:
                stack.append(i)
            else:
                if i != stack[-1]:
                    stack.append(i)
                else:
                    stack.pop()

        return str("".join(stack))
