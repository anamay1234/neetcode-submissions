class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [-1] * (len(s) + 1)

        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            possible = False

            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    if dp[i+len(word)]:
                        possible = True

            dp[i] = possible

        return dp[0]


        def dfs(i):
            if i == len(s):
                return True

            if dp[i] != -1:
                return dp[i]

            possible = False

            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        possible = True

            dp[i] = possible
            return dp[i]

        return dfs(0)
        