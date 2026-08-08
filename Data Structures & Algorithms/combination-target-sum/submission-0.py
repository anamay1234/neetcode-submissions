class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, total, array):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(array.copy())
                return

            array.append(nums[i])
            # take same number
            dfs(i, total + nums[i], array)

            array.remove(nums[i])
            # don't take same number
            dfs(i+1, total, array)

        dfs(0, 0, [])
        return res