class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i, arr):
            if i >= len(nums):
                res.append(arr.copy())
                return 
            
            print(i)
            arr.append(nums[i])
            take = dfs(i+1, arr)

            arr.remove(nums[i])
            noTake = dfs(i+1, arr)

        dfs(0, [])
        return res

        
        