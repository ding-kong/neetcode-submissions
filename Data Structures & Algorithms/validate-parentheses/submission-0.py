class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set(["{", "(", "["])
        for c in s:
            if c in opening:
                stack.append(c)
                continue

            # closing cases

            if len(stack) <= 0:
                return False

            v = stack.pop()
            if (v == "{" and c == "}") or (v == "(" and c == ")") or (v == "[" and c == "]"):
                continue
            
            return False
        
        return len(stack) == 0