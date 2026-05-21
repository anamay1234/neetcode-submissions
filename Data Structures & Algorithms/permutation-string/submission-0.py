class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # build s1 frequency only
        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1

        # sliding window over s2
        for i in range(n2):
            # add current char
            s2_counts[ord(s2[i]) - 97] += 1

            # remove char that slides out of window
            if i >= n1:
                s2_counts[ord(s2[i - n1]) - 97] -= 1

            # compare only when window size == n1
            if s1_counts == s2_counts:
                return True

        return False

            