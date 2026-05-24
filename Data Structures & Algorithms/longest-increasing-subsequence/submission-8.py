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

    # notes here for memo to tabu
    # prevInd in memo went from -1 -> n-1
    # thus prevInd in tabu should do from n-1 to -1

    # Just like in memo values of prevInd were stored in [prevInd + 1]
    # Similarlly, in tabu, storing values of prevInd in our dp should be done with [prevInd + 1]
    # since memo = dp table
    # However don't blindly just change every prevInd -> prevInd + 1.
    # For ex: nums[prevInd] shouldnt become nums[prevInd+1] in tabu
    # because we only do prevInd+1 in regards to storing in the memo/dp table.
    # nums[prevInd] is just accessing the value in array.
    # thus just like how in memo we didn't do nums[prevInd+1] for accessing in array, we don't
    # do here either.

    # Always change convert if to elif in tabu, it causes problem

    # in memo we did return self.func(0, -1, nums, dp)
    # but in tabu we did return dp[0][0] - dp[0][-1+1]

    # answer is need to realize that in the memo, 
    # the answer to self.func(0, -1) is stored in memo[0][0] cuz of prevIndex+1