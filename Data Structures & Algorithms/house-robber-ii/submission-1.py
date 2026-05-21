class Solution:
    def func(self, nums):
        dp = [-1] * len(nums)

        dp[0] = nums[0]
        for index in range(1, len(nums)):
            rob = nums[index] 
            if index-2 >= 0:
                rob += dp[index-2]

            not_rob = 0 + dp[index-1]

            dp[index] = max(rob, not_rob)


        return dp[len(nums) - 1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        noFirstHouse = nums[1:]
        noLastHouse = nums[:len(nums) - 1]
        return max(self.func(noFirstHouse), self.func(noLastHouse))