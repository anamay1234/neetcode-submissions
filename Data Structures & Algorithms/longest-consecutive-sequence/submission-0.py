class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSequence = 0
        coolSet = set(nums)
        i = 0

        for i in range(len(nums)):
            num = nums[i]

            # if this num is a start of a sequence
            if num - 1 not in coolSet:
                count = 1
                while num + 1 in coolSet:
                    count += 1
                    num = num + 1
                
                longestSequence = max(longestSequence, count)
        
        return longestSequence

        
        