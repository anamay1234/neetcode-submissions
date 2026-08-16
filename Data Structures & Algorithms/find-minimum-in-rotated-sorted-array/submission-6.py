class Solution:
    def findMin(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1
        minimum = nums[0]

        while L <= R:

            M = (L + R) // 2

            # left side is sorted
            if nums[L] <= nums[M]:
                minimum = min(nums[L], minimum)
                L = M + 1
            else:
                minimum = min(nums[M], minimum)
                R = M - 1

        return minimum



        