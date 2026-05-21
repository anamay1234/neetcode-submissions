class Solution:

    def climbStairs(self, n: int) -> int:
        # My Tabu approach
        arr = [0] * (n+1)

        arr[0] = 1
        for stairNum in range(1, n+1):
            oneStep = arr[stairNum - 1]
            twoStep = 0

            if (stairNum - 2) >= 0:
                twoStep = arr[stairNum - 2]
            arr[stairNum] = oneStep + twoStep
            

        return arr[n]

    

        
        