class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        count = 0
        visited = set()
        cycle = False
        

        def dfs(node, prevNode):
            if node in visited:
                nonlocal cycle
                cycle = True
                return
            
            nonlocal count
            count += 1
            visited.add(node)
            
            for nei in graph[node]:
                if nei is not prevNode:
                    dfs(nei, node)

            return

        dfs(0, None)
        if cycle == True:
            return False
        else:
            return count == n
        
        