class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)
        
        dp[0] = nums[0]

        for ind in range(1, len(nums)):
            rob = nums[ind]
            if ind - 2 >= 0:
                rob += dp[ind - 2]

            noRob = 0 + dp[ind - 1]

            dp[ind] = max(rob, noRob)
        
        return dp[len(nums) - 1]
            

        def dfs(ind):
            if ind == 0:
                return nums[ind]

            if dp[ind] != -1:
                return dp[ind]

            rob = nums[ind]
            if ind - 2 >= 0:
                rob += dfs(ind - 2)

            noRob = 0 + dfs(ind - 1)

            dp[ind] = max(rob, noRob)
            return dp[ind]

        return dfs(len(nums) - 1)

        