class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            stone1 -= stone2
            if stone1:
                heapq.heappush(stones, -stone1)
            
        return -stones[0] if len(stones) > 0 else 0