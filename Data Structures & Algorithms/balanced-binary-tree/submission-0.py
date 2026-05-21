# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        returner = True
        def dfs(curr):
            if curr is None:
                return 0

            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            if abs(leftHeight - rightHeight) > 1:
                nonlocal returner
                returner = False
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return returner

