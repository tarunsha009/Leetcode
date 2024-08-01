# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        res = []

        q = deque([root])
        flag = True

        while q:
            ans = []
            for _ in range(len(q)):
                curr = q.popleft()
                ans.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if flag:
                flag = False
            else:
                ans.reverse()
                flag = True
            
            res.append(ans)

        return res