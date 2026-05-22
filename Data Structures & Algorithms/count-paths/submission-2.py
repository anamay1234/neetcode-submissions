class Solution:
    # tabu
    def func(self, i, j, dp):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        goUp = self.func(i - 1, j, dp)
        goLeft = self.func(i, j - 1, dp)

        dp[i][j] = goUp + goLeft
        return dp[i][j]
        
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for i in range(m)]

        dp[0][0] = 1
        
        for i in range(0, m):
            for j in range(0, n):
                # write this to skip the base case
                # cuz we can still have to fill stuff like dp[0][1] dp[0][2]
                # or dp[1][0] dp[2][0] dp[3][0]
                if i == 0 and j == 0:
                    continue

                goUp = 0
                if i - 1 >= 0:
                    goUp = dp[i - 1][j]
                
                goLeft = 0
                if j - 1 >= 0:
                    goLeft = dp[i][j - 1]

                dp[i][j] = goUp + goLeft


        return dp[m - 1][n - 1]

# Note the following base case can't be intalized in dp array
# therefore we must handle it inside our loop with an if statement 
#    if i < 0 or j < 0:
#      return 0
# 