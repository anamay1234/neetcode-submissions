class Solution:
    # brute force
    def func(self, i, j, matrix, dp):

        if dp[i][j] != -1:
            return dp[i][j]

        canGoSomewhere = False
        up, down, left, right = 0, 0, 0, 0
        if i - 1 >= 0 and matrix[i][j] < matrix[i-1][j]:
            up = 1 + self.func(i - 1, j, matrix, dp)
            canGoSomewhere = True
        if i + 1 <= len(matrix) - 1 and matrix[i][j] < matrix[i+1][j]:
            down = 1 + self.func(i + 1, j, matrix, dp)
            canGoSomewhere = True
        
        if j - 1 >= 0 and matrix[i][j] < matrix[i][j-1]:
            left = 1 + self.func(i, j - 1, matrix, dp)
            canGoSomewhere = True

        if j+1 <= len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j+1]:
            right = 1 + self.func(i, j + 1, matrix, dp) 
            canGoSomewhere = True

        if canGoSomewhere == True:
            dp[i][j] = max(up, down, left, right)
            return dp[i][j]
        else:
            dp[i][j] = 1 + max(up, down, left, right)
            return dp[i][j]
  

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = [[-1] * len(matrix[0]) for i in range(len(matrix))]

        longestPath = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longestPath = max(longestPath, self.func(i, j, matrix, dp))
        return longestPath