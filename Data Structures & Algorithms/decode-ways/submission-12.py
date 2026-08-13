class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [-1] * len(s)

        if s[0] != "0":
            dp[0] = 1
        if s[0] == "0":
            dp[0] = 0

        for i in range(1, len(s)):

            oneDigit = 0
            # 1 digit
            if s[i] != "0":
                oneDigit = dp[i - 1] 


            twoDigit = 0
            # 2 digit
            if i - 1 >= 0 and int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26: 
                if i - 2 == -1:
                    twoDigit = 1
                else:
                    twoDigit = dp[i - 2]

            dp[i] = oneDigit + twoDigit

        return dp[len(s) - 1]

        
        def dfs(i):
            if i < 0:
                return 1
            if i == 0:
                if s[0] != "0":
                    return 1
                if s[0] == "0":
                    return 0

            if dp[i] != -1:
                return dp[i]

            oneDigit = 0
            # 1 digit
            if s[i] != "0":
                oneDigit = dfs(i - 1) 


            twoDigit = 0
            # 2 digit
            if i - 1 >= 0 and int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26: 
                twoDigit = dfs(i - 2)

            dp[i] = oneDigit + twoDigit
            return dp[i]

            

        return dfs(len(s) - 1)