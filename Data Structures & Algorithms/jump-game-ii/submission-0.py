class Solution:
    # striver vid
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        L = 0
        R = 0

        while (R < len(nums) - 1):

            farthest = 0
            for index in range(L, R+1):
                farthest = max(farthest, index+nums[index])

            L = R + 1
            R = farthest
            jumps += 1
        
        return jumps

        
