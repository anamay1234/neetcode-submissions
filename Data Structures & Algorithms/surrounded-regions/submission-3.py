class Solution:
    # my code
    def func(self, i, j, board): # used to temporaryily convert border O's to a placeholder
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 'X' or board[i][j] == 'placeholderforO':
            return

        board[i][j] = 'placeholderforO'

        self.func(i - 1, j, board)
        self.func(i + 1, j, board)
        self.func(i, j - 1, board)
        self.func(i, j + 1, board)


    def solve(self, board: List[List[str]]) -> None:

        for i in range(len(board)):     
            if board[i][0] == 'O':
                self.func(i, 0, board)

            if board[i][len(board[0]) - 1] == 'O':
                self.func(i, len(board[0]) - 1, board)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.func(0, j, board)

            if board[len(board) - 1][j] == 'O':
                self.func(len(board) - 1, j, board)
        
        print(board)

        for i in range(len(board)):
            for j in range(len(board[0])):

                # filling in surrounded Regions
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                # reverting Back
                if board[i][j] == 'placeholderforO':
                    board[i][j] = 'O'




# replace any 'O's starting at border with a placeholder 
# and any 'O's connected to the border 'O's.
# 
# Then the only 'O's left in theboard must be surrounded.
# Those O's should be converted to 'X'

# Finally revert the 'O's at the border and their connected 'O's back to 'O'
        