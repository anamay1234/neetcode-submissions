# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return res

        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                topElement = q.popleft()
                level.append(topElement.val)
                if topElement.left is not None:
                    q.append(topElement.left)
                if topElement.right is not None:
                    q.append(topElement.right)
            
            res.append(level)

        return res
        