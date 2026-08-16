class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # for each position find what is the largest rectangle u can make
        # For each position find:
        # pse (previous smaller element index)
        # nse (next smaller element index)
        # then rectangle = heights[i] * (nse - pse - 1)

        pse = self.pse(heights)
        nse = self.nse(heights)

        maxRec = 0

        for i in range(len(heights)):
            currRectangle = heights[i] * (nse[i] - pse[i] - 1)
            maxRec = max(maxRec, currRectangle)

        return maxRec



    def pse(self, heights):
        stack = []
        pse = [-1] * len(heights)

        for i in range(len(heights)):

            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if stack:
                pse[i] = stack[-1][1]

            stack.append([heights[i], i])

        return pse

    def nse(self, heights):
        stack = []
        nse = [len(heights)] * len(heights)

        for i in range(len(heights) - 1, -1, -1):

            while stack and stack[-1][0] >= heights[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1][1]

            stack.append([heights[i], i])

        return nse

        