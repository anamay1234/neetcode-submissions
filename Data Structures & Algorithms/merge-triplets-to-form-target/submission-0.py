class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                triplets.remove(trip)

        xPossible = False
        yPossible = False
        zPossible = False
        for trip in triplets:
            if trip[0] == target[0]:
                xPossible = True
            if trip[1] == target[1]:
                yPossible = True
            if trip[2] == target[2]:
                zPossible = True

        return xPossible and yPossible and zPossible