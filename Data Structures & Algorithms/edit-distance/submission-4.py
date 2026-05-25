class Solution:
    # memo
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

        # took care of i = n 
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # took care of j = m
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # now we only need to worry about these cases
        #  i: n - 1 -> 0     
        #  j  m - 1 -> 0   
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    # 0 cuz no operations needed to be performed
                
                    dp[i][j] = 0 + dp[i+1][j+1]
                
                if word1[i] != word2[j]:
                    insert = 1 + dp[i][j + 1]
                    delete = 1 + dp[i + 1][j]
                    replace = 1 + dp[i + 1][j + 1]

                    dp[i][j] = min(insert, delete, replace)
        
        return dp[0][0]


# i: 0 -> n     [n+1]
# j  0 -> m     [m+1]

# i: n -> 0     [n+1]
# j  m -> 0     [m+1]

# took care of i = n 

# base cases
# states in loops (backwards)
# copy recurence
