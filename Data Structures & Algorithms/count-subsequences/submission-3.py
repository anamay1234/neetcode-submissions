class Solution:
    # memo
    def func(self, i, j, s, t, dp):
        if j == len(t):
            return 1

        if i == len(s):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] == t[j]:
            pick = self.func(i+1, j+1, s, t, dp)
            noPick = self.func(i+1, j, s, t, dp)

            dp[i][j] = pick + noPick
            return dp[i][j]
        
        if s[i] != t[j]:
            noPick = self.func(i+1, j, s, t, dp)

            dp[i][j] = noPick
            return dp[i][j]
        

    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1] * (len(t) + 1) for i in range(len(s) + 1)]
        return self.func(0, 0, s, t, dp)

        # i: 0 -> len(s)
        # j: 0 -> len(t)