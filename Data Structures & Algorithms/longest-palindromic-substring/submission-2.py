class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longestLen = 0

        for i in range(len(s)):

            # odd len
            L, R = i, i
            while L >= 0 and R <= len(s) - 1 and s[L] == s[R]:
                if R - L + 1 > longestLen:
                    longestLen = (R - L + 1)
                    longest = s[L:R+1]
                L -= 1
                R += 1

            # even len
            L, R = i, i+1
            while L >= 0 and R <= len(s) - 1 and s[L] == s[R]:
                if R - L + 1 > longestLen:
                    longestLen = (R - L + 1)
                    longest = s[L:R+1]
                L -= 1
                R += 1

        return longest

        