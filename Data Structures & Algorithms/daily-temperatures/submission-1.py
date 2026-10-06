class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):

            if len(stack) == 0:
                stack.append([temp, i])
            else:

                while stack and stack[-1][0] < temp:
                    prevTemp, ind = stack.pop()

                    res[ind] = i - ind

                stack.append([temp, i])

        return res
        