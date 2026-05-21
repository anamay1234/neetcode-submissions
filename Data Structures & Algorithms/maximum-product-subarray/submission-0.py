class Solution:
    # striver vid
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxProduct = float('-inf')


        for i in range(len(nums)):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1

            # going forward
            prefix = prefix * nums[i]
            # going backwards
            suffix = suffix * nums[len(nums) - 1 - i]

            maxProduct = max(maxProduct, prefix, suffix)

        return maxProduct