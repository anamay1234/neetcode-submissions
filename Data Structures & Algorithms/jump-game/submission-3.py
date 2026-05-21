class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #striver

        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False

            farthestIndexWeCanReach = i + nums[i]
            if farthestIndexWeCanReach > max_index:
                max_index = farthestIndexWeCanReach
            
            if max_index >= len(nums) - 1:
                return True

        #    curr_location = 4
        #        0 1 2 3 4
        #        1 2 0 1 0