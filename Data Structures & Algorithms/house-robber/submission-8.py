class Solution:
    # Tabu - striver DP 5
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-1] * n
        dp[0] = nums[0]

        for i in range(1, n):
            pick = nums[i]

            if i - 2 >= 0:
                pick += dp[i - 2]
                
            notPick = 0 + dp[i - 1]

            dp[i] = max(pick, notPick)

        return dp[n-1]
