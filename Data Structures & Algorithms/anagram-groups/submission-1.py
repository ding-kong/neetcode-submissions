from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def _rep(s: str):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            d = {a: 0 for a in alphabet}
            for c in s:
                d[c] += 1
            key = ""
            for a in alphabet:
                if d[a] > 0:
                    key = f"{key}{a}{d[a]}"
            return key
        
        groups = defaultdict(lambda: [])
        for s in strs:
            groups[_rep(s)].append(s)
        
        return list(groups.values())