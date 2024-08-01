# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        ans = 0

        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                ans += curr.val
            if curr.left and low < curr.val:
                stack.append(curr.left)
            if curr.right and high > curr.val:
                stack.append(curr.right)
        
        return ans
        