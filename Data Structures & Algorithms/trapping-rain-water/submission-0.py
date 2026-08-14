class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxLeft, maxRight = 0, 0
        total = 0

        while L < R:
            # put water left side
            if height[L] <= height[R]:
                # check if i can put water here
                if height[L] < maxLeft:
                    total += maxLeft - height[L]
                else:
                    maxLeft = height[L]
                L += 1
            # put water right side
            else:
                # check if i can put water here
                if height[R] < maxRight:
                    total += maxRight - height[R]
                else:
                    maxRight = height[R]
                R -= 1

        return total
                    

           



    
    # decide which side to put water on left or right
    # this is decided based on which side is smaller as that is the 
    # thing that decides if you can put water or not

    # then see if you can put water on that side or not by comparing to maxOfThatSide
        

        