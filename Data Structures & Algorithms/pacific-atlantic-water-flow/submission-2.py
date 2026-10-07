class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(i, j, ocean, prevHeight):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] < prevHeight or (i, j) in ocean:
                return
            
            ocean.add((i, j))

            dfs(i+1, j, ocean, heights[i][j])
            dfs(i-1, j, ocean, heights[i][j])
            dfs(i, j+1, ocean, heights[i][j])
            dfs(i, j-1, ocean, heights[i][j])
        

        pacific = set()
        atlantic = set()

        for j in range(len(heights[0])):
            dfs(0, j, pacific, heights[0][j])
            dfs(len(heights) - 1, j, atlantic, heights[len(heights) - 1][j])

        for i in range(len(heights)):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, len(heights[0]) - 1, atlantic, heights[i][len(heights[0]) - 1])

        res = []
        for coordinates in pacific:
            if coordinates in atlantic:
                x, y = coordinates
                res.append([x, y])

        return res

