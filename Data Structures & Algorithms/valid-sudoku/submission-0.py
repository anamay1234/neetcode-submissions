class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        nums = set()

        for row in range(len(board)):
            nums.clear()

            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if int(board[row][col]) in nums:
                        return False
                    nums.add(int(board[row][col]))


            nums.clear()

        for col in range(len(board[0])):
                nums.clear()

                for row in range(len(board)):
                    if board[row][col] != ".":
                        if int(board[row][col]) in nums:
                            return False
                        nums.add(int(board[row][col]))

        nums.clear()

        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                nums.clear()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col] != ".":
                            if int(board[row][col]) in nums:
                                return False
                            nums.add(int(board[row][col]))
        
        return True





        
        print(board)
        return True