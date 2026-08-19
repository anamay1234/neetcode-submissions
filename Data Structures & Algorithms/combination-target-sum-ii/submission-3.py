class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def dfs(i, total, arr):
            if total == target:
                # if arr not in res:
                res.append(arr.copy())
                return
            if total > target or i >= len(candidates):
                return


            arr.append(candidates[i])
            take = dfs(i+1, total + candidates[i], arr)

            arr.pop()

            while (i+1) <= len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1


            take = dfs(i+1, total, arr)


        
        dfs(0, 0, [])
        return res
        