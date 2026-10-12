from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(lambda: 0)
        for c in s:
            d[c] = d[c] + 1
        for c in t:
            if c not in d:
                return False
            d[c] -= 1
            if d[c] == 0:
                del d[c]
        return len(d) == 0