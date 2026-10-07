class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        numFresh = 0
        minutes = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numFresh += 1

                if grid[i][j] == 2:
                    q.append((i, j))

        

        while q and numFresh != 0:

            for _ in range(len(q)):
                a, b = q.popleft()
                
                d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for x, y in d:
                    newA = a + x
                    newB = b + y

                    if newA < 0 or newB < 0 or newA >= len(grid) or newB >= len(grid[0]):
                        continue

                    if grid[newA][newB] == 1:
                        numFresh -= 1
                        grid[newA][newB] = 2
                        q.append((newA, newB))

                    
            minutes += 1

        return minutes if numFresh == 0 else -1

        