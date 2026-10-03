class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxA = 0

        L = 0
        R = len(heights) - 1

        while L <= R:
            maxA = max(maxA, min(heights[L], heights[R]) * (R - L))

            if min(heights[L], heights[R]) == heights[L]:
                L += 1
            else:
                R -= 1


        return maxA
        