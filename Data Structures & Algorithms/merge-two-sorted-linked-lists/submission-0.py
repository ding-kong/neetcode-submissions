# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            
            if l1.val <= l2.val:
                res = rec(l1.next, l2)
                l1.next = res
                return l1

            res = rec(l1, l2.next)
            l2.next = res
            return l2
        
        return rec(list1, list2)