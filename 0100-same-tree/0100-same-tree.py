# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def dfs(t1: Optional[TreeNode], t2: Optional[TreeNode]):
        #     if t1 is None and t2 is None:
        #         return
        
        #     if t1.val != t2.val:
        #         return False
        #     dfs(t1.left, t2.left)
        #     dfs(t1.right, t2.right)
        #     return True
        # return dfs(p,q)

        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right


        