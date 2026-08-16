class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        LROW = 0
        RROW = ROWS - 1

        while LROW <= RROW:
            MROWINDEX = (LROW + RROW) // 2
            MROW = matrix[MROWINDEX]
            print(MROW)

            if target >= MROW[0] and target <= MROW[COLS - 1]:
                break

            elif target < MROW[0]:
                RROW = MROWINDEX - 1
            else:
                LROW = MROWINDEX + 1

        if LROW >= ROWS or RROW < 0:
            return False

        row = MROW
        L = 0
        R = len(row) - 1

        while L <= R:
            M = (L + R) // 2

            if row[M] == target:
                return True
            elif row[M] < target:
                L = M + 1
            else:
                R = M - 1

        return False
        