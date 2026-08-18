class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-1 * stones[i] for i in range(len(stones))]
        heapq.heapify(stones)

        while len(stones) > 1:
            heavierStone = heapq.heappop(stones) * -1
            lighterStone = heapq.heappop(stones) * -1

            if heavierStone == lighterStone:
                continue
            else:
                newStone = (heavierStone - lighterStone) * -1
                heapq.heappush(stones, newStone)

            
        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0

        