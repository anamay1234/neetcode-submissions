class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited, cycle = set(), set()
        componentCount = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)

            
        for edge in range(n):
            if edge not in visited:
                dfs(edge)
                componentCount += 1
        return componentCount