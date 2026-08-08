class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == "0":
                return

            visited.add((i, j))
    
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            


        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    print(i, j)
                    dfs(i, j)
                    count += 1
        
        return count
                
        