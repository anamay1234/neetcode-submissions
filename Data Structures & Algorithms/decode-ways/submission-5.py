class Solution:
    def func(self, s, ind, dp):
        # reached end
        if ind == len(s):
            return 1
        # invalid, can't decode anymore
        if s[ind] == "0":
            return 0
        
        if dp[ind] != -1:
            return dp[ind]

        # take first digit
        firstDigit = self.func(s, ind+1, dp)
        # take first 2 digits
        firstTwoDigits = 0
        if ind + 2 <= len(s) and int(s[ind:ind+2]) <= 26:
            firstTwoDigits = self.func(s, ind+2, dp)

        dp[ind] = firstDigit + firstTwoDigits
        return dp[ind]


    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        dp[len(s)] = 1

        for ind in range(len(s) - 1, -1, -1):
            if s[ind] == "0":
                dp[ind] = 0
            else:
                # take first digit
                firstDigit = dp[ind+1]
                # take first 2 digits
                firstTwoDigits = 0
                if ind + 2 <= len(s) and int(s[ind:ind+2]) <= 26:
                    firstTwoDigits = dp[ind+2]

                dp[ind] = firstDigit + firstTwoDigits

        return dp[0]
    
        