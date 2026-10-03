class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        L = 0
        R = len(height) - 1

        maxLeft = 0
        maxRight = 0

        while L <= R:
            if height[L] <= height[R]:
                if maxLeft > height[L]:
                    total += maxLeft - height[L]
                else:
                    maxLeft = max(maxLeft, height[L])

                L += 1
            else:
                if maxRight > height[R]:
                    total += maxRight - height[R]
                else:
                    maxRight = max(maxRight, height[R])

                R -= 1
        
        return total

                
        