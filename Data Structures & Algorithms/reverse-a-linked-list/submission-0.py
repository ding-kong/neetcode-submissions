# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_prev, p = None, head

        while p:
            p_next = p.next
            p.next, p_prev, p = p_prev, p, p_next
        
        return p_prev