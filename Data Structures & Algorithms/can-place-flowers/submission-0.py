class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def safe_check(arr, i, limit):
            if i < 0:
                return 0
            if i >= limit:
                return 0
            return arr[i]

        _len, i = len(flowerbed), 0

        while i < _len and n > 0:
            val = safe_check(flowerbed, i-1, _len) == 0 and safe_check(flowerbed, i, _len) == 0 \
                and safe_check(flowerbed, i+1, _len) == 0
            if val:
                n -= 1
                i += 2
                continue
            i += 1
        
        return n <= 0