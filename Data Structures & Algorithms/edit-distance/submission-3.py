class Solution:
    # brute force
    def func(self, i, j, word1, word2, dp):
        if i == len(word1):
            # number of insert operations needed 
            return len(word2) - j
        
        if j == len(word2):
            # number of delete operations needed
            return len(word1) - i

        if dp[i][j] != -1:
            return dp[i][j]

        if word1[i] == word2[j]:
            # 0 cuz no operations needed to be performed
        
            dp[i][j] = 0 + self.func(i+1, j+1, word1, word2, dp)
            return dp[i][j]
        
        if word1[i] != word2[j]:
            insert = 1 + self.func(i, j + 1, word1, word2, dp)
            delete = 1 + self.func(i + 1, j, word1, word2, dp)
            replace = 1 + self.func(i + 1, j + 1, word1, word2, dp)

            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]

        


    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * (len(word2) + 1)  for i in range(len(word1) + 1)]
        return self.func(0, 0, word1, word2, dp)


# i: 0 -> n     [n+1]
# j  0 -> m     [m+1]
