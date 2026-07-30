class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        L, R = 0, len(clean_text) - 1
        while L <= R:
            if clean_text[L] == clean_text[R]:
                L += 1
                R -= 1
                continue
            else:
                return False
            
        return True
