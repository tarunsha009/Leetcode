# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        queue = deque([root])
        res = []
        max_so_far = float("-inf")

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                max_so_far = max(max_so_far, curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            # curr = stack.pop()
            # max_so_far = max(max_so_far, curr.val)
            res.append(max_so_far)
            # if curr.right:
            #     stack.append(curr.right)
            # if curr.left:
            #     stack.append(curr.left)
            
        return res
        