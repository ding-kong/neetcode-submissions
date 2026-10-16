# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(p: Optional[TreeNod]) -> (int, int):     # (diameter, depth)
            if not p:
                return (0, 0)
            if not p.left and not p.right:
                (0, 1)
            
            left_diameter, left_depth = rec(p.left)
            right_diameter, right_depth = rec(p.right)

            return (max(left_depth + right_depth, left_diameter, right_diameter), 1 + max(left_depth, right_depth))
        
        diameter, _ = rec(root)
        return diameter