# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(p: Optional[TreeNode]) -> Optional[TreeNode]:
            if (not p) or not (p.left or p.right):
                return p
            p.right, p.left = rec(p.left), rec(p.right)
            return p
        return rec(root)