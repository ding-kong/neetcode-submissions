# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []

        curr = [root]

        while curr:
            res.append([p.val for p in curr])

            nxt = []
            for p in curr:
                if p.left:
                    nxt.append(p.left)
                if p.right:
                    nxt.append(p.right)

            curr = nxt
        
        return res