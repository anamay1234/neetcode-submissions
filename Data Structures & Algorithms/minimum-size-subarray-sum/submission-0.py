class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLength = float('inf')
        runningSum = 0

        L = 0
        for R in range(len(nums)):
            
            runningSum += nums[R]

            while runningSum >= target:
                minLength = min(R - L + 1, minLength)
                runningSum -= nums[L]
                L += 1

        return minLength if minLength != float('inf') else 0





        