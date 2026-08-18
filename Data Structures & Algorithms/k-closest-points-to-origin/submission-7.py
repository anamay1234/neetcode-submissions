class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        for x, y in points:
            distances.append([((x-0)**2 + (y-0)**2)**0.5, [x, y]])


        print(distances)
        heapq.heapify(distances)

        res = []
        
        for i in range(k):
            point = heapq.heappop(distances)
            res.append(point[1])

        return res





        