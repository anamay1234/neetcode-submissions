class Solution:
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

    # My Tabulation
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last_index = len(cost) - 1
        dp = [-1] * len(cost)


        dp[0] = cost[0]
        dp[1] = cost[1]

        for index in range(2, len(cost)):
            
            goFromOneFloorBelow = cost[index] + dp[index-1]
            goFromTwoFloorBelow = 101
            if index - 2 >= 0:
                goFromTwoFloorBelow = cost[index] + dp[index-2]

            dp[index] = min(goFromOneFloorBelow, goFromTwoFloorBelow)

        
        return min(dp[last_index-1], dp[last_index])