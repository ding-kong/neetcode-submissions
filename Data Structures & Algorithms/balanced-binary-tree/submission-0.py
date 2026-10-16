# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(p: Optional[TreeNode]) -> (bool, int): # balanced, depth
            if not p:
                return (True, 0)
            is_left_balanced, left_depth = rec(p.left)
            if not is_left_balanced:
                return (False, -1)
            is_right_balanced, right_depth = rec(p.right)
            if not is_right_balanced:
                return (False, -1)
            
            return (abs(left_depth - right_depth) <= 1, 1 + max(left_depth, right_depth))

        is_balanced , _ = rec(root)
        return is_balanced