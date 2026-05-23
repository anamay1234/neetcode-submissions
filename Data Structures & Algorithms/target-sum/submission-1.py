class Solution:
    def func(self, ind, target, nums):
        if ind == len(nums):
            if target == 0:
                return 1
            if target > 0 or target < 0:
                return 0

        pos = self.func(ind + 1, target + nums[ind], nums)
        neg = self.func(ind + 1, target - nums[ind], nums)

        return pos + neg

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.func(0, target, nums)

        # Recursion
        #  f(index, target)
        #  2 stuffs - either assign positive or negative
        #  sum up total ways of both stuffs
        #
        # base case (target == 0) = return 1 cuz total ways
        #
        #
        # Note: every number must be used exactly once, and each one gets either + or -
        # thus base case can only be at ind == 0

        