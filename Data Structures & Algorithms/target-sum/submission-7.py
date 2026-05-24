class Solution:
    # brute force
    def func(self, ind, target, nums):
        if ind == 0:
            if target == 0 and nums[0] == 0:
                return 2
            if target == 0 or target == nums[0]:
                return 1
            else:
                return 0

        notTake = self.func(ind - 1, target, nums)
        take = 0
        if target >= nums[ind]:
            take = self.func(ind - 1, target - nums[ind], nums)

        return notTake + take

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        totalSum = sum(nums)
        if (totalSum - target) < 0 or (totalSum - target) % 2:
            return 0

        k = (totalSum - target) // 2
        return self.func(len(nums) - 1, k, nums)

        # Target Sum = Count Partitions With Given Difference 
        # divide array into 2 subsets (a positive subset, a negative subset)
        # such that subset1 - subset2 = target
        # return total ways


        