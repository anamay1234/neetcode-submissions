class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Use minheap to get start of next cardGroup
        # If it is in the minHeap, there must be atleast 1 occurance in the # in hashmap
        # If minheap is empty, no more groups to create, thus return True

        hashmap = {}
        for card in hand:
            hashmap[card] = 1 + hashmap.get(card, 0)

        hand.clear()
        hand = list(hashmap.keys())

        heapq.heapify(hand)
        while hand:
            if hand:
                minValue = hand[0]
                hashmap[minValue] -= 1

                if hashmap[minValue] == 0:
                    heapq.heappop(hand)

            prevNum = minValue
            for counter in range(groupSize - 1):
                if not hand:
                    return False
                if hand:
                    if prevNum + 1 not in hashmap:
                        return False


                    hashmap[prevNum + 1] -= 1
                    if hashmap[prevNum + 1] == 0:
                        heapq.heappop(hand)
                    prevNum = prevNum + 1
        return True
            

                