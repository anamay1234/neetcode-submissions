class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        need = len(countT)
        have = 0

        L = 0
        minSubString = ""
        minSubStringLength = float('inf')
        windowCount = {}

        for R in range(len(s)):
            if s[R] in countT:
                windowCount[s[R]] = windowCount.get(s[R], 0) + 1
                if windowCount[s[R]] == countT[s[R]]:
                    have += 1
            

            while have == need:
                if R - L + 1 < minSubStringLength:
                    minSubStringLength = R - L + 1
                    minSubString = s[L:R+1]

                if s[L] in windowCount:
                    windowCount[s[L]] -= 1
                    if windowCount[s[L]] < countT[s[L]]:
                        have -= 1
                L += 1

        return minSubString
                    
                        







