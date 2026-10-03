class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            if i == 0:
                res[i] = prefix
            else:
                prefix = prefix * nums[i - 1]
                res[i] = prefix

        postfix = 1

        for i in range(len(res) - 1, -1, -1):
            if i == len(res) - 1:
                res[i] *= postfix
            else:
                postfix *= nums[i+1]
                res[i] *= postfix

        return res



        