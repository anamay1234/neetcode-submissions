class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        returnArray = [1] * len(nums)

        # Prefixs
        prefix = 1
        
        for i in range(len(nums)):
            if i-1 < 0:
                returnArray[i] = prefix
            else:
                returnArray[i] = prefix * nums[i-1]
                prefix = returnArray[i]
            
        # PostFix
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            if i+1 >= len(nums):
                returnArray[i] = returnArray[i]
            else:
                postfix = nums[i+1] * postfix
                returnArray[i] = postfix * returnArray[i]
        
        return returnArray
                

        