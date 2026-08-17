# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        flag = True
        
        def dfs(node):
            if node is None:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if abs(leftHeight - rightHeight) > 1:
                nonlocal flag
                flag = False
            
            return 1 + max(leftHeight, rightHeight)



        dfs(root)
        return flag
            


