class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.heap = []
        self.closestPoints = []
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            if len(self.heap) < k:
                heapq.heappush(self.heap, -distance)
                self.closestPoints.append(point)
            else:
                if distance < -self.heap[0]:
                    heapq.heappush(self.heap, -distance)
                    shortDistance = -heapq.heappop(self.heap)
                    i = 0
                    for closePoint in self.closestPoints:
                        if shortDistance == math.sqrt((closePoint[0])**2 + (closePoint[1])**2):
                            self.closestPoints.pop(i)
                            self.closestPoints.append(point)
                            break
                        i += 1
                    
        return self.closestPoints