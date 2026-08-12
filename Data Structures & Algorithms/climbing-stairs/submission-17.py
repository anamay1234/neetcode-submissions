class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n+1)

        dp[0] = 1

        for stairNum in range(1, n+1):
            oneStep = dp[stairNum - 1]
            twoStep = 0
            if stairNum - 2 >= 0:
                twoStep = dp[stairNum - 2]

            dp[stairNum] = oneStep + twoStep
            


        return dp[n]




        