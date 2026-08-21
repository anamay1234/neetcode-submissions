class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi = float("-inf")
        runningSum = 0

        for num in nums:

            runningSum += num
            maxi = max(maxi, runningSum)

            if runningSum < 0:
                runningSum = 0
            
        return maxi