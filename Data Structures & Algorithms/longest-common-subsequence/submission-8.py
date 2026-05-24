class Solution:
    # tabu
    def func(self, i, j, text1, text2, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        # matching
        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.func(i - 1, j - 1, text1, text2, dp)
            return dp[i][j]

        # not matching
        if text1[i] != text2[j]:
            
            tryByUpdatingStr1 = self.func(i - 1, j, text1, text2, dp) 
            tryByUpdatingStr2 = self.func(i, j - 1, text1, text2, dp)

            dp[i][j] = max(tryByUpdatingStr1, tryByUpdatingStr2)
            return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for i in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                # matching
                if text1[i] == text2[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else: 
                        dp[i][j] = 1 + 0
                # not matching
                elif text1[i] != text2[j]:
                    if i - 1 >= 0:        
                        tryByUpdatingStr1 = dp[i - 1][j]
                    else: 
                        tryByUpdatingStr1 = 0
                    
                    if j - 1 >= 0:
                        tryByUpdatingStr2 = dp[i][j - 1]
                    else:
                        tryByUpdatingStr2 = 0

                    dp[i][j] = max(tryByUpdatingStr1, tryByUpdatingStr2)

        return dp[len(text1) - 1][len(text2) - 1]

# Note: In tabulation we can't initalize the base case:
#         if i < 0 or j < 0:
#            return 0
# since we can't access negative values in our dp table,
# hence we must deal with this base case by writing an if statement in our for loop
#
#
#


33

