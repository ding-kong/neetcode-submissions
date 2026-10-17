# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        p_val = min(p.val, q.val)
        q_val = max(p.val, q.val)

        # while curr.val != p.val and curr.val != q.val and not (curr)
        while not (p_val <= curr.val <= q_val):
            print(p_val, curr.val, q_val)
            if curr.val < p_val:
                curr = curr.right
            else:
                curr = curr.left
        
        return curr