# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        self.dfs(root)
        return self.maxi

    def dfs(self, node):
        if node is None:
            return 0
        
        leftSum = max(0, self.dfs(node.left))
        rightSum = max(0, self.dfs(node.right))

        self.maxi = max(self.maxi, leftSum + node.val + rightSum)

        return node.val + max(leftSum, rightSum)




        