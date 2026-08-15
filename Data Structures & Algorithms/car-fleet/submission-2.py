class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        newStorer = []
        for i in range(len(position)):
            newStorer.append([position[i], speed[i]])

        newStorer.sort()

        stack = []
        for i in range(len(position) - 1, -1, -1):
            # check if other cars behind will catch up to this car and make car fleet
            if stack:
                prevCarPos, prevCarSpeed = stack[-1]

                prevCartime = (target - prevCarPos) / prevCarSpeed

                currCarTime = (target - newStorer[i][0]) / newStorer[i][1]

                if prevCartime >= currCarTime:
                    continue
                else:
                    stack.append(newStorer[i])
            else:
                stack.append(newStorer[i])

        return len(stack)



        