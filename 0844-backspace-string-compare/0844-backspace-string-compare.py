class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        # for i in s:
        #     if stack1 and i == '#':
        #         stack1.pop()
        #     else:
        #         stack1.append(i)
        for i in s:
            if i != '#':
                stack1.append(i)
            elif stack1:
                stack1.pop()

        # for j in t:
        #     if stack2 and j == '#':
        #         stack2.pop()
        #     else:
        #         stack2.append(j)
        for j in t:
            if j !='#':
                stack2.append(j)
            elif stack2:
                stack2.pop()
        
        return stack1 == stack2