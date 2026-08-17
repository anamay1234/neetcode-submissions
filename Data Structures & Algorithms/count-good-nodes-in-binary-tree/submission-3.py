# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, prevValue):
            if node is None:
                return 0

            if node.val >= prevValue:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            elif node.val < prevValue:
                return 0 + dfs(node.left, prevValue) + dfs(node.right, prevValue)


        return dfs(root, float("-inf"))
        