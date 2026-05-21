class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #striver Jump Game - I

        max_index = 0
        for i in range(len(nums)):
            # we reach an index that is ahead of the farthest max index could have reached

            if i > max_index:
                return False

            currentfarthestIndexWeCanReach = i + nums[i]
            if currentfarthestIndexWeCanReach > max_index:
                max_index = currentfarthestIndexWeCanReach
            
            if max_index >= len(nums) - 1:
                return True

        #    curr_location = 4
        #        0 1 2 3 4
        #        1 2 0 1 0