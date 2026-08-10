class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        noRobLastHouse = self.helperFunc(nums[0:len(nums) - 1])
        noRobFirstHouse = self.helperFunc(nums[1:len(nums)])
        return max(noRobLastHouse,noRobFirstHouse )

    def helperFunc(self, nums):
        dp = [-1] * len(nums)
        
        dp[0] = nums[0]

        for ind in range(1, len(nums)):
            rob = nums[ind]
            if ind - 2 >= 0:
                rob += dp[ind - 2]

            noRob = 0 + dp[ind - 1]

            dp[ind] = max(rob, noRob)
        
        return dp[len(nums) - 1]
        