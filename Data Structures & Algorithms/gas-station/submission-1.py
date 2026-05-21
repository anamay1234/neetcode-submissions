class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # now we know there exists an answer

        startPos = 0
        gasTank = 0
        for i in range(len(gas)):
            gasTank += gas[i] - cost[i]

            # If I can’t reach the next station from our start, 
            # nobody between this start and failure point can either.
            # Thus lets try from next startPosition and reset the gasTank
            if gasTank < 0:
                startPos = i + 1
                gasTank = 0

        return startPos


