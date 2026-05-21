class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Initialize queue and count fresh
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        time = 0

        while q:
            size = len(q)
            rotted_this_round = False

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != 1
                    ):
                        continue

                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
                    rotted_this_round = True

            # Only increment time if we actually rotted something
            if rotted_this_round:
                time += 1

        return time if fresh == 0 else -1