class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        mpsOne = {}
        mpsTwo = {}

        for s in s1:
            mpsOne[s] = mpsOne.get(s, 0) + 1

        L = 0

        for R in range(len(s2)):

            mpsTwo[s2[R]] = mpsTwo.get(s2[R], 0) + 1

            if R - L + 1 > len(s1):
                mpsTwo[s2[L]] -= 1
                if mpsTwo[s2[L]] == 0:
                    del mpsTwo[s2[L]]
                L += 1

                  
            if R - L + 1 == len(s1):
                if mpsOne == mpsTwo:
                    return True

        return False
            
            


            

            



            
            

        