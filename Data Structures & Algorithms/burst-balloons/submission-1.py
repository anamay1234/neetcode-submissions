class Solution:
    # brute force striver 51
    def func(self, i, j, nums, dp):
        if (i > j):
            return 0
        maxi = float('-inf')

        if dp[i][j] != -1:
            return dp[i][j]
            
        for ind in range(i, j+1):
            amntOfCoins = nums[i - 1] * nums[ind] * nums[j+1] + self.func(i, ind-1, nums, dp) + self.func(ind+1, j, nums, dp)
            maxi = max(maxi, amntOfCoins)

        dp[i][j] = maxi
        return dp[i][j]

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for i in range(n+1)]
        nums.insert(0, 1)
        nums.append(1)
        
        return self.func(1, n, nums, dp)

# max value of i = n [n+1]
# max value of j = n [n+1]