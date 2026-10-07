class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        visited = set()
        cnt = 0

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):

            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                cnt += 1
        
        return cnt 
        