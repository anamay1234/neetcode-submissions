class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make a max heap (negative values)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # pop max value
            x = heapq.heappop(stones) * -1
            # pop 2nd max value
            y = heapq.heappop(stones) * -1

            if x - y > 0:
                heapq.heappush(stones, (x-y)*-1)

        return 0 if len(stones) == 0 else (stones[0] * -1)
        