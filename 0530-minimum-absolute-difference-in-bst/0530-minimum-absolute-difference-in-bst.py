# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return
            left = dfs(root.left)
            arr.append(root.val)
            right = dfs(root.right)
        
        arr = []
        dfs(root)
        min_diff = float("inf")
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        return min_diff
        