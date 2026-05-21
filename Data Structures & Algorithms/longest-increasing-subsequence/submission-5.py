class Solution:
    # memo
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
        return self.func(0, -1, nums, dp)