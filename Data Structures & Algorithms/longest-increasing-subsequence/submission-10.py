class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [[-1] * (len(nums) + 2) for _ in range(len(nums) + 1)]
        
        def dfs(i, prev):
            if i == len(nums):
                return 0

            if dp[i][prev + 1] != -1:
                return dp[i][prev + 1]

            if prev == -1:
                take = 1 + dfs(i+1, i)
                dontTake = dfs(i+1, prev)
                
                dp[i][prev + 1] = max(take, dontTake)
                return dp[i][prev + 1]
            else:
                take = 0
                if nums[prev] < nums[i]:
                    take = 1 + dfs(i+1, i)
                dontTake = dfs(i+1, prev)

                dp[i][prev + 1] = max(take, dontTake)
                return dp[i][prev + 1]

        return dfs(0, -1)



            


        