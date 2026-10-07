class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)


        # check if we can get to every single node
        # no cycles
        
        visited = set()
        count = 0

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            nonlocal count
            count += 1
            # print(node, count)

            res = False

            for nei in graph[node]:
                print(nei)
                if nei != prev:
                    if dfs(nei, node) == False:
                        return False

            return True


        return dfs(0, -1) and count == n




        
        
        