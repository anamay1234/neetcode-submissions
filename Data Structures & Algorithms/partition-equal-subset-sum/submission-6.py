class Solution:
    # tabu
    def func(self, ind, target, nums, dp):
        if target == 0:
            return True
        if ind == 0:
            return nums[0] == target
    
        if dp[ind][target] != -1:
            return dp[ind][target]

        pick = False
        if target - nums[ind] >= 0:
            pick = self.func(ind - 1, target - nums[ind], nums, dp)

        notPick = self.func(ind - 1, target, nums, dp)

        dp[ind][target] = pick or notPick
        return dp[ind][target]


    def canPartition(self, nums: List[int]) -> bool:
        #starting part
        sum_total = 0
        for i in range(len(nums)):
            sum_total += nums[i]
        if sum_total % 2 != 0:
            return False
        else:
            target = sum_total // 2
            dp = [[False] * (target + 1) for i in range(len(nums))]

            for ind in range(len(nums)):
                dp[ind][0] = True
            
            for target in range(target + 1):
                dp[0][target] = nums[0] == target

            for ind in range(1, len(nums)):
                for target in range(1, target + 1):
                    pick = False
                    if target - nums[ind] >= 0:
                        pick = dp[ind - 1][target - nums[ind]]

                    notPick = dp[ind - 1][target]

                    dp[ind][target] = pick or notPick

            return dp[len(nums) - 1][target]


