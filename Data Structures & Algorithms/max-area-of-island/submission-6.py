class Solution:
    # my code
    def func(self, i, j, grid, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in visited:
            return 0

        visited.add((i, j))
        print(i, j)

        left = self.func(i, j - 1, grid, visited)
        right = self.func(i, j + 1, grid, visited)
        up = self.func(i - 1, j, grid, visited)
        down = self.func(i + 1, j, grid, visited)

        return 1 + left + right + up + down

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, self.func(i, j, grid, visited))


        return maxArea
        