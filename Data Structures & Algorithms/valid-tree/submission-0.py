class Solution:
    # me
    def dfs(self, node, prev, graph, visited):
        if node in visited:
            return False
        
        visited.add(node)

        for neigh in graph[node]:
            if neigh != prev:
                if self.dfs(neigh, node, graph, visited) == False:
                    return False
            
        return True
                

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # req1 - all nodes have to be connected
        # req2 - no cycles allowed

        # do a dfs, add each visited node to a visited set
        # if in our dfs we can ever return back to a node from the node we started from
        # it has a cycle, thus return false
        # This takes care of req2
        # Once done, check if count of nodes visited len(visitedSet) == n
        # This takes care of req1

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()

        # starting at a random node 0, it doesn't matter cuz 
        # any node should connect to all the other if its valid
        if self.dfs(0, -1, graph, visited) == False:
            # we got a cycle
            return False

        return len(visited) == n


