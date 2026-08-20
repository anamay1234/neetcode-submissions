class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        q = deque()

        countFresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1: 
                    countFresh += 1

        while q and countFresh > 0:

            for _ in range(len(q)):
                fruit = q.popleft()
                x = fruit[0]
                y = fruit[1]

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for r, c in directions:
                    newX = x + r
                    newY = y + c
                    if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and grid[newX][newY] == 1:
                        
                        grid[newX][newY] = 2
                        q.append((newX, newY))
                        countFresh -= 1

            minutes += 1

        if countFresh == 0:
            return minutes
        else:
            return -1
