from bisect import bisect_left
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= k <= max(piles)
        # binary search on k
        # sum([ceil(pile/k) for pile in piles])
        # check this against <= h

        def can_finish(k: int) -> int:
            return sum([ceil(pile/k) for pile in piles]) <= h

        speeds = range(1, max(piles)+1)
        i = bisect_left(speeds, True, key=can_finish)
        return i+1