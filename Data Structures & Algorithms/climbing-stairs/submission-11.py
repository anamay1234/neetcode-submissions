class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n+1)

        def dfs(stairNum):
            if stairNum == 1:
                return 1
            if stairNum == 2:
                return 2

            if dp[stairNum] != -1:
                return dp[stairNum]
            
            dp[stairNum] = dfs(stairNum - 1) + dfs(stairNum - 2) 
            return dp[stairNum]

        return dfs(n)


        