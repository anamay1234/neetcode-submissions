class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        # store the islands from where water can reach an ocean
        pacific = set()
        atlantic = set()

        def dfsFlowChecker(r, c, ocean, previousHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < previousHeight or (r, c) in ocean:
                return
            ocean.add((r, c))
            dfsFlowChecker(r + 1, c, ocean, heights[r][c])
            dfsFlowChecker(r - 1, c, ocean, heights[r][c])
            dfsFlowChecker(r, c + 1, ocean, heights[r][c])
            dfsFlowChecker(r, c - 1, ocean, heights[r][c])

        # adding the islands from where water can reach an ocean 
        for r in range(rows):
            dfsFlowChecker(r, 0, pacific, heights[r][0])
            dfsFlowChecker(r, cols - 1, atlantic, heights[r][cols - 1])


        for c in range(cols):
            dfsFlowChecker(0, c, pacific, heights[0][c])
            dfsFlowChecker(rows - 1, c, atlantic, heights[rows - 1][c])

        # at this point we have added all the adjecent islands to the sets
        # now lets start working on the inner islands

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])


        return result



        
        
        

    
        