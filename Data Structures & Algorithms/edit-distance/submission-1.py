class Solution:
    # brute force
    def func(self, i, j, word1, word2, dp):
        if i < 0:
            # number of insert operations needed 
            return j + 1
        
        if j < 0:
            # number of delete operations needed
            return i + 1

        if dp[i+1][j+1] != -1:
            return dp[i+1][j+1]

        if word1[i] == word2[j]:
            # 0 cuz no operations needed to be performed
            dp[i+1][j+1] =  0 + self.func(i-1, j-1, word1, word2, dp)
            return dp[i+1][j+1]
        
        if word1[i] != word2[j]:
            insert = 1 + self.func(i, j - 1, word1, word2, dp)
            delete = 1 + self.func(i - 1, j, word1, word2, dp)
            replace = 1 + self.func(i - 1, j - 1, word1, word2, dp)

            dp[i+1][j+1] = min(insert, delete, replace) 
            return dp[i+1][j+1]

        


    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * (len(word2) + 1)  for i in range(len(word1) + 1)]
        return self.func(len(word1) - 1, len(word2) - 1, word1, word2, dp)


# i: n - 1 -> -1     [n+1]
# j  m - 1 -> -1     [m1]

# -1 0 1 n-1        (values in reality)
#  0 1 2 n          (where we will store them in dp)