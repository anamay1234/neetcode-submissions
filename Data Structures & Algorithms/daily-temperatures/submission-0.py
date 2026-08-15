class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # check if any of the days at the top of stack have a smaller temp
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append([temperatures[i], i])

        return res



        