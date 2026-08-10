class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs startni on every node

        visited = set()
        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)


        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)



        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
            
        return count
