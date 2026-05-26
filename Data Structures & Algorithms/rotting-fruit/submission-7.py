class Solution:
    # my code
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # first find all rotten fruit indexs,
        # then add all rotten fruit to the starting queue of bfs, 
        # then do the multistart bfs with a minute counter
        # each iteration of bfs is +1 minute
        
        minuteCount = 0
        freshCount = 0
        nodesPerLevel = 0

        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    nodesPerLevel += 1
                if grid[i][j] == 1:
                    freshCount += 1

        while queue and freshCount > 0:

            newNodesPerLevel = 0
            for i in range(nodesPerLevel):
                i, j = queue.popleft()

                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    freshCount -= 1
                    newNodesPerLevel += 1
                    up = (i-1, j)
                    queue.append(up)
                
                if i+1 <= len(grid) - 1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    freshCount -= 1
                    newNodesPerLevel += 1
                    down = (i+1, j)
                    queue.append(down)
                
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    freshCount -= 1
                    newNodesPerLevel += 1
                    left = (i, j-1)
                    queue.append(left)
                
                if j+1 <= len(grid[0]) - 1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    freshCount -= 1
                    newNodesPerLevel += 1
                    right = (i, j+1)
                    queue.append(right)

            nodesPerLevel = newNodesPerLevel
            minuteCount += 1
            print(minuteCount)


        return minuteCount if freshCount == 0 else -1