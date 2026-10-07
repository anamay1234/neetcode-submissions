class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2147483647


        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        cnt = 1

        while q:
            for _ in range(len(q)):
                a, b = q.popleft()

                d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for x, y in d:
                    newA = a + x
                    newB = b + y
                    if newA < 0 or newA >= len(grid) or newB < 0 or newB >= len(grid[0]):
                        continue

                    if grid[newA][newB] == INF:
                        grid[newA][newB] = cnt
                        q.append((newA, newB))

            cnt += 1



        