class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        hashmap = {}

        for i, num in enumerate(nums):

            if target - num not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[target - num], i]

