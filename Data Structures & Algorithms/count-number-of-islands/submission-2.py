class Solution:
    # my solution - striver
    def dfs(self, i, j, grid, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == "0":
            return

        visited.append((i,j))

        up = self.dfs(i-1, j, grid, visited)
        down = self.dfs(i+1, j, grid, visited)
        left = self.dfs(i, j-1, grid, visited)
        right = self.dfs(i, j+1, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid) # number of rows 
        n = len(grid[0]) # number of cols

        visited = list()
        islandCount = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.dfs(i, j, grid, visited)
                    islandCount += 1

        print(visited)

        return islandCount
         
        