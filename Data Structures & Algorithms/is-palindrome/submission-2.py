import re

class Solution:
    def alphaNum(self, c):
        ord_c = ord(c)
        return (ord('A') <= ord_c <= ord('Z')) or \
               (ord('a') <= ord_c <= ord('z')) or \
               (ord('0') <= ord_c <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i < j:
            while i < j and not self.alphaNum(s[i]):
                i+=1

            while i < j and not self.alphaNum(s[j]):
                j-=1
            
            print("compare ", s[i], s[j])

            if s[i].lower() != s[j].lower():
                return False
            
            i, j = i+1, j-1
        
        return True
            

    # def isPalindrome(self, s: str) -> bool:
    #     s2 = re.sub(r'[^a-z0-9]', '', s.lower())
    #     return s2 == s2[::-1]