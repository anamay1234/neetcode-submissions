class Solution:
    def findMin(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1
        minimum = float('inf')

        while L <= R:
            M = (L + R) // 2

            # left side is sorted
            if nums[L] <= nums[M]:
                minimum = min(minimum, nums[L])
                L = M + 1
            # right side is sorted
            elif nums[M] < nums[R]:
                minimum = min(minimum, nums[M])
                R = M - 1


        return minimum
        