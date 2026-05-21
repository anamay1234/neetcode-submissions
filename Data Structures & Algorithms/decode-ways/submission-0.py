class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]
            
            # take 1 digit and add its result
            
            ways = dfs(i+1)

            # take 2 digits add its result
            if i+2 <= len(s) and int(s[i:i+2]) <= 26:
                ways += dfs(i+2)

            memo[i] = ways
            return ways

        return dfs(0)


        