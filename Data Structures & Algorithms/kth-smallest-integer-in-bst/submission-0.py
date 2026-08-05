# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = 0
        count = 0
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)

            nonlocal count, ans
            count += 1
            if count == k:
                ans = node.val
            
            dfs(node.right)

        dfs(root)
        return ans