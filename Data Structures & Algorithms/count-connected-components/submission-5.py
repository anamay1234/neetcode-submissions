class Solution:
    # my solution
    def dfs(self, node, graph, visited):
        
        visited.add(node)

        for connectedNode in graph[node]:
            if connectedNode not in visited:
                self.dfs(connectedNode, graph, visited)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # hashmap - node : list of connected nodes
        graph = defaultdict(list)

        for edge in range(n):
            graph[edge]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        
        visited = set()
        count = 0

        for node in graph.keys():
            if node not in visited:
               self.dfs(node, graph, visited)
               count += 1

        return count