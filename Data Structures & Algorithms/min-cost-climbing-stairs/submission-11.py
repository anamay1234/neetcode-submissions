class Solution:
    # My Memo Force
    def func(self, index, cost, dp):
        if index == 0 or index == 1:
            return cost[index]

        if dp[index] != -1:
            return dp[index]

        goFromOneFloorBelow = cost[index] + self.func(index-1, cost, dp)
        goFromTwoFloorBelow = 101
        if index - 2 >= 0:
            goFromTwoFloorBelow = cost[index] + self.func(index-2, cost, dp)

        dp[index] = min(goFromOneFloorBelow, goFromTwoFloorBelow)
        return dp[index]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last_index = len(cost) - 1

        dp = [-1] * len(cost)
        
        return min(self.func(last_index-1, cost, dp), self.func(last_index, cost, dp))