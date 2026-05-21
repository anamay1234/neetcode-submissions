class Solution:
    def checkValidString(self, s: str) -> bool:
        # striver vid

        leastPossibleOpen = 0
        mostPossibleOpen = 0
        for i in range(len(s)):
            if s[i] == "(":
                leastPossibleOpen += 1
                mostPossibleOpen += 1
            if s[i] == ")":
                leastPossibleOpen -= 1
                mostPossibleOpen -= 1
            if s[i] == "*":
                leastPossibleOpen -= 1
                mostPossibleOpen += 1

            if mostPossibleOpen < 0:
                return False

            if leastPossibleOpen < 0:
                leastPossibleOpen = 0

        return leastPossibleOpen == 0

# count must be equal to 0 at end for a valid paranthesis string to be possible