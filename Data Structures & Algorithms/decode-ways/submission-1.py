class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            # If we've reached the end, it's a valid decoding
            if i >= len(s):
                return 1

            # If current char is '0', no valid decoding
            if s[i] == "0":
                return 0

            # Return cached result
            if i in memo:
                return memo[i]
            
            # Take one digit
            ways = dfs(i+1)

            # Take two digits if valid (10 to 26)
            if i+2 <= len(s) and int(s[i:i+2]) <= 26:
                ways += dfs(i+2)

            memo[i] = ways
            return ways

        return dfs(0)


        