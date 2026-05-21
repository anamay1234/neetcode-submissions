# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#bfs and get all nodes per level, then take all the last values of the nodes per level

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            levelLength = len(queue)
            nodesPerLevel = []

            for i in range(levelLength):
                node = queue.popleft()
                nodesPerLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            lastValueInLevel = nodesPerLevel[levelLength - 1]
            result.append(lastValueInLevel)

        return result

            



        