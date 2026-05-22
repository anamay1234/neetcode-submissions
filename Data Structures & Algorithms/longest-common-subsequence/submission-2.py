class Solution:
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
        return self.func(len(text1) - 1, len(text2) - 1, text1, text2, dp)