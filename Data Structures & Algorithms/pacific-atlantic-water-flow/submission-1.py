class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacificSet = set()
        atlanticSet = set()

        def dfs(i, j, setToAddTo, prevHeight):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] < prevHeight or (i, j) in setToAddTo:
                return

            setToAddTo.add((i, j))
            dfs(i+1, j, setToAddTo, heights[i][j])
            dfs(i-1, j, setToAddTo, heights[i][j])
            dfs(i, j+1, setToAddTo, heights[i][j])
            dfs(i, j-1, setToAddTo, heights[i][j])



        # bordering rows
        for j in range(len(heights[0])):
            dfs(0, j, pacificSet, heights[0][j])
            dfs(len(heights) - 1, j, atlanticSet, heights[len(heights) - 1][j])

        # bordering cols
        for i in range(len(heights)):
            dfs(i, 0, pacificSet, heights[i][0])
            dfs(i, len(heights[0]) - 1, atlanticSet, heights[i][len(heights[0]) - 1])

        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacificSet and (i, j) in atlanticSet:
                    res.append([i,j])

        return res








