from heapq import heappop, heappush, heapreplace, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        h = [-stone for stone in stones]
        heapify(h)
        
        while len(h) >= 2:
            first = heappop(h)
            second = heappop(h)
            diff = first-second
            if diff != 0:
                heappush(h, first-second)
        
        return -heappop(h) if len(h) == 1 else 0