class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()
        longest = 0

        L = 0
        for R in range(len(s)):

            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1
            hashset.add(s[R])
            longest = max(longest, R - L + 1)

        return longest





        