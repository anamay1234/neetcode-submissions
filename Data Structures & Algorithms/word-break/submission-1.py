class Solution:
    def func(self, ind, s, wordDict, dp):
        if ind == len(s):
            return True

        if dp[ind] != -1:
            return dp[ind]

        stringSuccessfullSeperation = False

        for word in wordDict:
            if ind + len(word) <= len(s) and s[ind:ind+len(word)] == word:
                substringSuccessfullSperation = self.func(ind+len(word), s, wordDict, dp)
                if substringSuccessfullSperation == True:
                    stringSuccessfullSeperation = True

        dp[ind] = stringSuccessfullSeperation
        return dp[ind]



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * (len(s) + 1)
        return self.func(0, s, wordDict, dp)