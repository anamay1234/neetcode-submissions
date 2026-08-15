class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hasht = {}

        for c in t:
            hasht[c] = hasht.get(c, 0) + 1

        hashs = {}
        string = ""
        shortestStringLen = float('inf')

        have = 0
        need = len(hasht)

        L = 0

        for R in range(len(s)):
            if s[R] in hasht:
                hashs[s[R]] = hashs.get(s[R], 0) + 1
                if hashs[s[R]] == hasht[s[R]]:
                    have += 1

            while have == need:
                if R - L + 1 < shortestStringLen:
                    shortestStringLen = R - L + 1
                    string = s[L:R+1]

                if s[L] in hashs:
                    hashs[s[L]] -= 1
                    if hashs[s[L]] < hasht[s[L]]:
                        have -= 1
                L += 1


        return string




        



        