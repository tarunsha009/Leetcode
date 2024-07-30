class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # if len(s) < 2:
        #     return False
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                
                if i == ")" and stack[-1] == "(" or i == "}" and stack[-1] == "{" or i == "]" and stack[-1] == "[":
                    stack.pop()
        
        return len(stack) == 0
        