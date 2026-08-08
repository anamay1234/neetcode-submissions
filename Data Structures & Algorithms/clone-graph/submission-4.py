"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# DFS
# Create Node
# Go to all neighbors
    # Append neighbors to current Node
# return Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        visited = set()
        hashmap = {}

        def dfs(node):

            newNode = Node(node.val)
            hashmap[node] = newNode

            for nei in node.neighbors:
                if nei in hashmap:
                    newNode.neighbors.append(hashmap[nei])
                else:
                    newNode.neighbors.append(dfs(nei))
            
            return newNode

        return dfs(node)




        