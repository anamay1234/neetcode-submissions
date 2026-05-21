class Solution:
    def longestPalindrome(self, s: str) -> str:
        # https://www.youtube.com/watch?v=0CKUjDcUYYA - good video
        # What is the Dp in this problem? Ans below
        # [L, R] = Palindrome if [L+1, R-1] && string[L] == string[R]
        # Thus repeated Work

        maxLength = 0
        maxStr = ""

        for i in range(len(s)):
            # odd case
            L = i
            R = i
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if (R - L + 1) > maxLength:
                        maxLength = R - L + 1
                        maxStr = s[L:R+1]
                    L -= 1
                    R +=1
                else:
                    break

            #even
            L = i
            R = i+1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if (R - L + 1) > maxLength:
                        maxLength = R - L + 1
                        maxStr = s[L:R+1]
                    L -= 1
                    R += 1
                else:
                    break
        return maxStr










