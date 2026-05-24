class Solution:
    # tabu
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

        dp[len(s1)][len(s2)] = True

        for ind1 in range(len(s1), -1, -1):
            for ind2 in range(len(s2), -1, -1):

                if ind1 == len(s1) and ind2 == len(s2):
                    continue # skip this case, taken case of by base case

                #  - take s1 digit if it matches f(ind1 - 1, ind2)

                takeDigitS1 = False
                takeDigitS2 = False
                if ind1 != len(s1) and s1[ind1] == s3[ind1 + ind2]:
                    takeDigitS1 = dp[ind1 + 1][ind2]

                #  - take s2 digit if it matches f(ind1, ind2 - 1)
                
                if ind2 != len(s2) and s2[ind2] == s3[ind1 + ind2]:
                    takeDigitS2 = dp[ind1][ind2 + 1]

                dp[ind1][ind2] = takeDigitS1 or takeDigitS2

        return dp[0][0]

# base case
# states in loops

    # ind1: n -> 0 [n+1]
    # ind2: m -> 0 [m+1]
    # But we took care of dp[n][m] with base case
    # so we need to skip that case in for loops

# copy recurence