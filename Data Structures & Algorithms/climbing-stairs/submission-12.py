class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n+1)

        dp[1] = 1
        if n >= 2:
            dp[2] = 2

        for stairNum in range(3, n+1):
            dp[stairNum] = dp[stairNum - 1] + dp[stairNum - 2]

        return dp[n]



        