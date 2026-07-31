class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxAreaE = 0

        L = 0
        R = len(heights) - 1

        while L < R:

            area = min(heights[L], heights[R]) * (R - L)
            maxAreaE = max(maxAreaE, area)

            if heights[L] <= heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1

        return maxAreaE

        