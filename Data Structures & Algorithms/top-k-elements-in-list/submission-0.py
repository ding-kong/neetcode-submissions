import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # form frequency list
        d = defaultdict(lambda: 0)
        for num in nums:
            d[num] += 1
        
        # then build priority queue
        h = [(-v, k) for k, v in d.items()]
        heapq.heapify(h)

        # fetch k number of them
        ret = []
        for i in range(k):
            _, v = heapq.heappop(h)
            ret.append(v)
        
        return ret