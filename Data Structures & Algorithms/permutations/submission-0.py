class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(arr, nums):
            if len(nums) == 0:
                res.append(arr.copy())
                return

            for i in range(len(nums)):
                arr.append(nums[i])
                dfs( arr, nums[:i] + nums[i+1:])
                arr.pop()

        
        dfs([], nums.copy())
        return res
        
        