class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())


        for n in range(len(s)):
            if (s[n] == s[len(s) - n - 1]):
                if ((n == len(s) - n - 1) or n == ((len(s) - n - 1) - 1)):
                    return True
                continue
            else:
                return False
        return True
