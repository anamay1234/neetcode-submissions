class Solution:
    def maxArea(self, heights: List[int]) -> int:
        [1,7,2,5,4,7,3,6]
        start = 0
        end = len(heights) - 1
        runningBiggestArea = 0
        tempTopArea = 0
        
        while start < end:
            # tempTopArea = height - width
            tempTopArea = min(heights[start], heights[end]) * (end - start)

            if (tempTopArea > runningBiggestArea):
                runningBiggestArea = tempTopArea

            if (heights[end] < heights[start]):
                end = end - 1
            elif (heights[end] > heights[start]):
                start = start + 1
            else: 
                # this is the case where heights[end] == heights[start]
                # over here it doesn't matter we can do end = end - 1 or start = start + 1
                end = end - 1 


        return runningBiggestArea
