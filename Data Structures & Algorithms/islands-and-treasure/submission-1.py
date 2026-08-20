class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        distance = 1

        while q:

            for _ in range(len(q)):
                poppers = q.popleft()
                r = poppers[0]
                c = poppers[1]

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    newX = r + x
                    newY = c + y
                    if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and grid[newX][newY] == 2147483647:
                        grid[newX][newY] = distance
                        q.append((newX, newY))
                

            distance += 1
