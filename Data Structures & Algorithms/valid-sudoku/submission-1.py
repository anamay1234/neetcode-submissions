class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            newset = set()
            for j in range(len(board[0])):
                if board[i][j] != "." and int(board[i][j]) in newset:
                    return False
                if board[i][j] != ".":
                    newset.add(int(board[i][j]))

        for j in range(len(board[0])):
            newset = set()
            for i in range(len(board)):
                if board[i][j] != "." and int(board[i][j]) in newset:
                    return False
                if board[i][j] != ".":
                    newset.add(int(board[i][j]))
        
        for a in range(0, 8, 3):
            for b in range(0, 8, 3):
                newset = set()

                for i in range(a, a+3):
                    for j in range(b, b+3):
                        print(i, j)
                        if board[i][j] != "." and int(board[i][j]) in newset:
                            return False
                        if board[i][j] != ".":
                            newset.add(int(board[i][j]))

        return True





        

        