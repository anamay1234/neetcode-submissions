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
        if (totalSum - target) < 0 or (totalSum - target) % 2:
            return 0

        k = (totalSum - target) // 2

        dp = [[-1] * (k + 1) for i in range(len(nums))]

        for target in range(k+1):
            if target == 0 and nums[0] == 0:
                dp[0][target] = 2
            elif target == 0 or target == nums[0]:
                dp[0][target] = 1
            else:
                dp[0][target] = 0
        
        for ind in range(1, len(nums)):
            for target in range(k+1):
                notTake = dp[ind - 1][target]
                take = 0
                if target >= nums[ind]:
                    take = dp[ind - 1][target - nums[ind]]

                dp[ind][target] = notTake + take

        return dp[len(nums) - 1][k]

# ind 0 -> n (n+1 size needed)
# target m -> 0 (m+1 size needed)
#