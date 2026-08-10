class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):

            # odd length
            count += self.func(i, i, s)


            # even length
            count += self.func(i, i+1, s)

        return count

    def func(self, L, R, s):
        count = 0

        while L >= 0 and R <= len(s) - 1 and s[L] == s[R]:
            count += 1
            L -= 1
            R += 1
        
        return count

