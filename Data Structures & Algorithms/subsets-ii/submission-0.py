class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        def dfs(i, arr):
            if i >= len(nums):
                res.append(arr.copy())
                return 

            arr.append(nums[i])
            take = dfs(i+1, arr)

            arr.pop()
            while i + 1 <= (len(nums) - 1) and nums[i] == nums[i+1]:
                i += 1

            noTake = dfs(i+1, arr)

        dfs(0, [])
        return res
        