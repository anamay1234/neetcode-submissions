class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res = []

        for i in range(len(position)):
            res.append([position[i], speed[i]])

        res.sort()

        stack = []

        for i in range(len(res) - 1, -1, -1):

            stack.append(res[i])

            if len(stack) >= 2:

                prevCarPos, prevCarSpeed = stack.pop()
                aheadCarPos, aheadCarSpeed = stack.pop()


                pTime = (target - prevCarPos) / prevCarSpeed
                aTime = (target - aheadCarPos) / aheadCarSpeed

                if pTime <= aTime:
                    stack.append([aheadCarPos, aheadCarSpeed])
                else:
                    stack.append([aheadCarPos, aheadCarSpeed])
                    stack.append([prevCarPos, prevCarSpeed])

        return len(stack)




            
        