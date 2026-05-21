class Solution:
    # memo with coordinate change (+1) for prevInd
    def func(self, ind, prevInd, nums, dp):
        if ind == len(nums):
            return 0

        if dp[ind][prevInd + 1] != -1:
            return dp[ind][prevInd + 1]

        # valid pick case
        if prevInd == -1 or nums[prevInd] < nums[ind]:
            # 2 options, pick or don't pick
            pick = 1 + self.func(ind + 1, ind, nums, dp)
            notPick = 0 + self.func(ind + 1, prevInd, nums, dp)

            dp[ind][prevInd + 1] = max(pick, notPick)
            return dp[ind][prevInd + 1]

        # invalid pick case
        if nums[prevInd] >= nums[ind]: 
            dp[ind][prevInd + 1] = 0 + self.func(ind + 1, prevInd, nums, dp)
            return dp[ind][prevInd + 1]
            
             

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * (len(nums) + 1) for i in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[len(nums)][i] = 0

        for ind in range(len(nums) - 1, -1, -1):
            for prevInd in range(len(nums) - 1, -2, -1):
                # valid pick case
                if prevInd == -1 or nums[prevInd] < nums[ind]:
                    # 2 options, pick or don't pick
                    pick = 1 + dp[ind + 1][ind+1]
                    notPick = 0 + dp[ind + 1][prevInd+1]

                    dp[ind][prevInd + 1] = max(pick, notPick)

                # invalid pick case
                elif nums[prevInd] >= nums[ind]: 
                    dp[ind][prevInd + 1] = 0 + dp[ind + 1][prevInd+1]

        return dp[0][-1+1]