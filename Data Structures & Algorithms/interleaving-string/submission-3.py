class Solution:
    # memo
    def func(self, ind1, ind2, s1, s2, s3, dp):
        if ind1 == len(s1) and ind2 == len(s2):
            return True

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

#   - take s1 digit if it matches f(ind1 - 1, ind2)

        takeDigitS1 = False
        if ind1 != len(s1) and s1[ind1] == s3[ind1 + ind2]:
            takeDigitS1 = self.func(ind1 + 1, ind2, s1, s2, s3, dp)

#   - take s2 digit if it matches f(ind1, ind2 - 1)

        takeDigitS2 = False
        if ind2 != len(s2) and s2[ind2] == s3[ind1 + ind2]:
            takeDigitS2 = self.func(ind1, ind2 + 1, s1, s2, s3, dp)

        dp[ind1][ind2] = takeDigitS1 or takeDigitS2
        return dp[ind1][ind2]


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[-1] * (len(s2) + 1) for i in range(len(s1) + 1)]
        return self.func(0, 0, s1, s2, s3, dp)