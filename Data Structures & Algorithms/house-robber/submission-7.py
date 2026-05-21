class Solution:
    # Tabu - striver DP 5
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        dp[0] = nums[0]

        for ind in range(1, n):
            pick = nums[ind]

            if ind - 2 >= 0:
                pick += dp[ind - 2]
            notPick = 0 + dp[ind - 1]

            dp[ind] = max(pick, notPick)

        return dp[n-1]
