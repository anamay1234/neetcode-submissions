class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}

        L = 0
        longest = 0

        for R in range(len(s)):
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1

            while (R - L + 1) - max(hashmap.values()) > k:
                hashmap[s[L]] -= 1
                L += 1

            longest = max(longest, (R - L + 1))
        
        return longest

            
        