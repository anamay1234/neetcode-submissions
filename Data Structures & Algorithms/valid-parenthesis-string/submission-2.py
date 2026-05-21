class Solution:
    def checkValidString(self, s: str) -> bool:
        # striver vid

        lowestPossibleOpen = 0
        highestPossibleOpen = 0
        for i in range(len(s)):
            if s[i] == "(":
                lowestPossibleOpen += 1
                highestPossibleOpen += 1
            if s[i] == ")":
                lowestPossibleOpen -= 1
                highestPossibleOpen -= 1
            if s[i] == "*":
                lowestPossibleOpen -= 1
                highestPossibleOpen += 1

            if highestPossibleOpen < 0:
                return False

            if lowestPossibleOpen < 0:
                lowestPossibleOpen = 0

        return lowestPossibleOpen == 0

# count must be equal to 0 at end for a valid paranthesis string to be possible