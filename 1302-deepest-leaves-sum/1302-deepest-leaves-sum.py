# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # def dfs(root):
        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     return max(left, right) + 1
        
        # max_depth = dfs(root)
        # print(max_depth)
        
        queue = deque([root])
        sum = 0
        while queue:
            sum = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)   
        return sum
        