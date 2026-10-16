# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
            _sum = sum((not (not first), not (not second)))
            if _sum == 0: # both None
                return True
            if _sum == 1: # only one is None
                return False
            if (first.val != second.val):
                return False
            
            res = rec(first.left, second.left)
            if not res:
                return False
            
            res = rec(first.right, second.right)
            return res
        
        return rec(p, q)
