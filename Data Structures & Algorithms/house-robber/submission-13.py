class Solution:
    # me tabu
    def func(self, index, nums, dp):
        if index == 0:
            return nums[0]
        
        if dp[index] != -1:
            return dp[index]

        rob = nums[index] 
        if index-2 >= 0:
            rob += self.func(index-2, nums, dp)
        not_rob = 0 + self.func(index-1, nums, dp)

        dp[index] = max(rob, not_rob)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        dp[0] = nums[0]
        for index in range(1, len(nums)):
            rob = nums[index] 
            if index-2 >= 0:
                rob += dp[index-2]

            not_rob = 0 + dp[index-1]

            dp[index] = max(rob, not_rob)


        return dp[len(nums) - 1]
     

    # intuition
    # Explore all valid ways to rob houses
    # Take max way

    # Recurence
    # 1) f(index) = max amount we can rob from (index -> 0)
    # 2) 
    #    rob house -> (i-2)
    #    not rob -> (i-1)
    # 3) take max
    #
    #
