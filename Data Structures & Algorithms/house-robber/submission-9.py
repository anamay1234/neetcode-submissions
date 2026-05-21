class Solution:
    # Tabu Space Optimize - striver DP 5
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
    
        prev = nums[0]
        prev2 = 0
        
        for i in range(1, n):
            take = nums[i]
            if i > 1:
                take += prev2
            
            not_take = 0 + prev
            
            curi = max(take, not_take)
            prev2 = prev
            prev = curi
        
        return prev