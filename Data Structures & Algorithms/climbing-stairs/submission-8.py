class Solution:
    def func(self, stairNum, arr):
        if stairNum == 0:
            return 1
        oneStep = self.func(stairNum - 1, arr)
        twoStep = 0
        if arr[stairNum] != -1:
            return arr[stairNum]

        if (stairNum - 2) >= 0:
            twoStep = self.func(stairNum - 2, arr)
        arr[stairNum] = oneStep + twoStep
        return arr[stairNum]
        

    def climbStairs(self, n: int) -> int:
        # My Memo approach
        arr = [0] * (n+1)

        arr[0] = 1
        for stairNum in range(1, n+1):
            oneStep = arr[stairNum - 1]
            twoStep = 0

            if (stairNum - 2) >= 0:
                twoStep = arr[stairNum - 2]
            arr[stairNum] = oneStep + twoStep
            

        return arr[n]

    

        
        