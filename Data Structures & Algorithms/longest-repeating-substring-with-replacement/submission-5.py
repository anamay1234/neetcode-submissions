class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # totalStringLength - maxCharOccurances <= k
        # k = 1
        # maxLength = 0
        # chars = 
        # L 
        # R
        # a a a b a b b 
        # 0 1 2 3 4 5 6

        maxLength = 0


        hashmap = {}
        maxFreq = 0

        L = 0

        for R in range(len(s)):


            hashmap[s[R]] = hashmap.get(s[R], 0) + 1
            maxFreq = max(hashmap.values())

            while ((R - L + 1) - maxFreq) > k:
                hashmap[s[L]] -= 1
                L += 1
                maxFreq = max(hashmap.values())
                
            maxLength = max(maxLength, R - L + 1)

        return maxLength
                

        