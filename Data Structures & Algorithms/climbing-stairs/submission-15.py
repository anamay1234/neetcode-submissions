class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n+1)

        def dfs(stairNum):
            if stairNum == 0:
                return 1
            if stairNum == 1:
                return 1

            if dp[stairNum] != -1:
                return dp[stairNum]
            
            oneStep = dfs(stairNum - 1)
            twoStep = dfs(stairNum - 2)

            dp[stairNum] = oneStep + twoStep
            return dp[stairNum]

        return dfs(n)




        