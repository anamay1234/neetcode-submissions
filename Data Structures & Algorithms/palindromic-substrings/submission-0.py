class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s)):
            # odd case
            L = i
            R = i
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    count += 1
                    L -= 1
                    R +=1
                else:
                    break

            #even
            L = i
            R = i+1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    count += 1
                    L -= 1
                    R += 1
                else:
                    break
        return count