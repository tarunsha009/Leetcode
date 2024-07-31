class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        abc = path.split('/')
        for i in abc:
            if i == '..' and len(stack) >=1:
                stack.pop()
            elif i != '' and i != '..' and i !='.':
                stack.append("/"+ i)

        return str("".join(stack)) if len(stack) >= 1 else "/"