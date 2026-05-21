class Solution:
    def checkValidString(self, s: str) -> bool:
        # striver vid

        minCount = 0
        maxCount = 0
        for i in range(len(s)):
            if s[i] == "(":
                minCount += 1
                maxCount += 1
            if s[i] == ")":
                minCount -= 1
                maxCount -= 1
            if s[i] == "*":
                minCount -= 1
                maxCount += 1

            if maxCount < 0:
                return False
            if minCount < 0:
                minCount = 0

        return minCount == 0

# count must be equal to 0 at end for a valid paranthesis string to be possible