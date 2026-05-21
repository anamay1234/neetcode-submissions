class Solution:
    # memo
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
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True

        for ind in range(len(s) - 1, -1, -1):

            stringSuccessfullSeperation = False

            for word in wordDict:
                if ind + len(word) <= len(s) and s[ind:ind+len(word)] == word:
                    substringSuccessfullSperation = dp[ind+len(word)]
                    print(ind, word, dp[ind + len(word)])
                    if substringSuccessfullSperation == True:
                        stringSuccessfullSeperation = True

            dp[ind] = stringSuccessfullSeperation

        return dp[0]