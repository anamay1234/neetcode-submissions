"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, visited, mp):

        
        new = Node(node.val)
        mp[node] = new

        for nei in node.neighbors:
            if nei in mp:
                new.neighbors.append(mp[nei])
            else:
                print(node.val)
                print
                new.neighbors.append(self.dfs(nei, visited, mp))

        return new

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        visited = set()
        mp = {}
        return self.dfs(node, visited, mp)
        
        