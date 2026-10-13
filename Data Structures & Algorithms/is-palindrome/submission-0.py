import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s.lower())
        s2 = re.sub(r'[^a-z0-9]', '', s.lower())
        print(s2)
        return s2 == s2[::-1]