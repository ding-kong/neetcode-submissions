class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        ind = 0
        while ind < len(s):
            val = ""
            while s[ind] != "#":
                val += s[ind]
                ind += 1
            ind +=1
            val = int(val)
            res.append(s[ind:(ind+val)])
            ind += val
            
        return res