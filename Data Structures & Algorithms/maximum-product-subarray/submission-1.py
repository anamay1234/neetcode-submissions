class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProd = float("-inf")
        
        leftProd = 1
        rightProd = 1

        for i in range(len(nums)):
            leftProd *= nums[i]
            maxProd = max(maxProd, leftProd)

            rightProd *= nums[len(nums) - 1 - i]
            maxProd = max(maxProd, rightProd)

            if leftProd == 0:
                leftProd = 1

            if rightProd == 0:
                rightProd = 1

        return maxProd
