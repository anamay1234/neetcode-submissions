class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        for point in points:
            point.append(((point[0]-0)**2 + (point[1]-0)**2) ** 0.5)
            # points now is [[x, y, distance], [x, y, distance]]
            point[0], point[2] = point[2], point[0]
            # points now is [[distance, x, y], [distance, x, y]]
        
        

        # heapify works on the basis of the first element in the array which is distance
        heapq.heapify(points)

        returningArray = []
        for i in range(k):
            #remove closest point
            appendToArray = heapq.heappop(points)

            #remove the distance
            appendToArray.pop(0)

            #swap y,x -> x,y
            appendToArray[0], appendToArray[1] = appendToArray[1], appendToArray[0]

            returningArray.append(appendToArray)
        
        return returningArray



        