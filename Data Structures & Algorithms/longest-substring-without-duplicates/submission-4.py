class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        chars = set()

        L = 0
 
        # maxLength = 3
        # chars = b, c
        #   L 
        #       R
        # a b c a b c b b
        # 0 1 2 3 4 5 6 7

        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            
            chars.add(s[R])
            maxLength = max(maxLength, R - L + 1)

        return maxLength
                

            
        