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

        for j in range(len(t) + 1):
            dp[len(s)][j] = 0

        for i in range(len(s) + 1):
            dp[i][len(t)] = 1


        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    pick = dp[i+1][j+1]
                    noPick = dp[i+1][j]

                    dp[i][j] = pick + noPick
                # converted this to elif or else also works cuz
                # in our recursion we only do one if statement
                # we don't want to do both
                # thus we must make sure we can only do one case and not both
                elif s[i] != t[j]: 
                    noPick = dp[i+1][j]

                    dp[i][j] = noPick

        return dp[0][0]


    # Base cases
    # States in loops (backwards)
    # Copy Recurence

    # n = len(s)
    # m = len(t)

    # Memo
        # i: 0 -> n [n+1]
        # j: 0 -> m [m+1]
    # Tabu
        # i: n -> 0
        # j: m -> 0

    # i = n & j = m already taken care of in base case,
    # thus start from i = n - 1, j = m - 1