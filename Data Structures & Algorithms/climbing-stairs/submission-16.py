class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for stairNum in range(2, n+1):
            oneStep = dp[stairNum - 1]
            twoStep = dp[stairNum - 2]

            dp[stairNum] = oneStep + twoStep
            


        return dp[n]




        