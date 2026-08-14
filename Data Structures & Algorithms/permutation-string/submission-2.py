class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashs1 = {}
        for c in s1:
            hashs1[c] = hashs1.get(c, 0) + 1

        L = 0

        hashs2 = {}

        for R in range(len(s2)):
            # invalid case causes L to move
            if s2[R] not in hashs1:
                while L <= R:
                    if s2[L] in hashs2:
                        hashs2[s2[L]] -= 1
                    L += 1


                

                    
            if s2[R] in hashs1:
                hashs2[s2[R]] = hashs2.get(s2[R], 0) + 1
                # if we got extra of this letter then we remove extra
                while hashs2[s2[R]] > hashs1[s2[R]]:
                    if s2[L] in hashs2:
                        hashs2[s2[L]] -= 1
                    L += 1  
                if hashs1 == hashs2:
                    return True
            



        return False
