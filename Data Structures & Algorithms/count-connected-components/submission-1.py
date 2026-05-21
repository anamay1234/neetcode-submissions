class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            #first we create an adjecny list - hashmap
            # do a traversal for each node 
            # 2 sets, 1st set takes the nodes that are already seen
            # in a previous traversal, thus if in a new traversal one
            # of the the old nodes is seen we can stop it as we know it is
            # a repeat of a previously done traversal
            # 2nd set will be the set of nodes seen so far in current traversal

        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited, cycle = set(), set()
        componentCount = 0

        def dfs(node):
            if node in visited:
                return False
            if node in cycle:
                return True
            
            cycle.add(node)
            for nei in adjList[node]:
                if dfs(nei) == False:
                    return False
            return True
            
        for edge in range(n):
            if dfs(edge) == True:
                for element in cycle:
                    visited.add(element)
                cycle.clear()
                componentCount += 1
        return componentCount
        

                        
