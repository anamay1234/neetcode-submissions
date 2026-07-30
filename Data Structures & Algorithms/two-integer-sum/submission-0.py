class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], ind]
            hashmap[num] = ind


        