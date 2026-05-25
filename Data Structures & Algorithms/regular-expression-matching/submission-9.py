class Solution:
    # brute force neetcode
    def func(self, i, j, s, p, dp):
        if i == len(s) and j == len(p):
            return True

        if j >= len(p):
            return False

        if dp[i][j] != -1:
            return dp[i][j]

        # current character match
        if i < len(s) and (s[i] == p[j] or p[j] == "."):
            match = True
        else:
            match = False

        # check if next character is '*'
        if (j + 1) <= len(p) - 1 and p[j + 1] == "*":
            #x* takes up 0 case
            dontUse = self.func(i, j + 2, s, p, dp)

            use = False
            #x* takes up atleast 1 case
            if match:
                use = self.func(i + 1, j, s, p, dp)
            
            dp[i][j] = dontUse or use
            return dp[i][j]

        if match == True:
            dp[i][j] = self.func(i + 1, j + 1, s, p, dp)
            return dp[i][j]

        if match == False:
            dp[i][j] = False
            return dp[i][j]
             

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1] * (len(p) + 1) for i in range(len(s) + 1)]
        return self.func(0, 0, s, p, dp)
        