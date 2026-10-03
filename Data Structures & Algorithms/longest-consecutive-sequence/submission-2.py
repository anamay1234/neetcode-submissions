class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)

        count = 0

        for num in nums:
            if num - 1 not in hashset:
                starting = num
                length = 0
                while starting in hashset:
                    length += 1
                    starting += 1

                count = max(count, length)
        
        return count



        