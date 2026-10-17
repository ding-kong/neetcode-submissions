# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_in(r: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
            if (not r) and (not sub):
                return True
            if (r and (not sub)) or ((not r) and sub):
                return False
            if r.val != sub.val:
                return False
            return check_in(r.left, sub.left) and check_in(r.right, sub.right)
        
        def rec(r: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
            if not r:
                return False
            if check_in(r, sub):
                return True
            # return rec(r.left, sub) or rec(r.right, sub)
            if r and r.left and rec(r.left, sub):
                print("go left")
                return True
            if r and r.right and rec(r.right, sub):
                print("go right")
                return True
            return False
        
        return rec(root, subRoot)
