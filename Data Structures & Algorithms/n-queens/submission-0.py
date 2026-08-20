class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for i in range(n)]


        def dfs(row, board):
            if row == len(board):
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(len(board[0])):
                if col not in cols and row + col not in posDiag and row - col not in negDiag:
                    board[row][col] = "Q"
                    cols.add(col)
                    posDiag.add(row + col)
                    negDiag.add(row - col)
                    dfs(row + 1, board)
                    board[row][col] = "."
                    cols.remove(col)
                    posDiag.remove(row + col)
                    negDiag.remove(row - col)

        

        dfs(0, board)

        print(res)
        return res

        
        