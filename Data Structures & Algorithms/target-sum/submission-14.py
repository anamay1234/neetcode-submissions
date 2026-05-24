class Solution:
    # memo
    def func(self, ind, target, nums, dp):
        if ind == 0:
            if target == 0 and nums[0] == 0:
                return 2
            if target == 0 or target == nums[0]:
                return 1
            else:
                return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        notTake = self.func(ind - 1, target, nums, dp)
        take = 0
        if target >= nums[ind]:
            take = self.func(ind - 1, target - nums[ind], nums, dp)

        dp[ind][target] = notTake + take
        return dp[ind][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        totalSum = sum(nums)
        if (totalSum + target) % 2:
            return 0

        k = (totalSum + target) // 2

        dp = [[-1] * (k + 1) for i in range(len(nums))]
        return self.func(len(nums) - 1, k, nums, dp)