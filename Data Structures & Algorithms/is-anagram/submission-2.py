class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        mp1 = {}
        mp2 = {}

        for i in range(len(s)):
            
            mp1[s[i]] = mp1.get(s[i], 0) + 1
            mp2[t[i]] = mp2.get(t[i], 0) + 1


        return mp1 == mp2

        

        

        