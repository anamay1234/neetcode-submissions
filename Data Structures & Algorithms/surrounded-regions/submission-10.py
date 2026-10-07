class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "X" or (i, j) in visited:
                return 
            
            board[i][j] = "P"
            visited.add((i, j))

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # start at 'O' on edge
        # populate all connected 'O's with a placeholder

        # go thru matrix and convert all remaining 'O' to 'x'
        # then convert all placeholders back to 'O'

        starters = set()
        visited = set()

        for i in range(len(board)):
            if board[i][0] == "O":
                starters.add((i, 0))
            
            if board[i][len(board[0]) - 1] == "O":
                starters.add((i, len(board[0]) - 1))

        for j in range(len(board[0])):
            if board[0][j] == "O":
                starters.add((0, j))

            if board[len(board) - 1][j] == "O":
                starters.add((len(board) - 1, j))

        print(starters)
        for x, y in starters:
            print(x, y)
            if (x, y) not in visited:
                dfs(x, y)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "P":
                    board[i][j] = "O"



        