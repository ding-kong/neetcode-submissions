# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head.next

        while fast:
            if fast == slow:
                return True
            if fast.next is None or fast.next.next is None:
                return False
            if fast.next == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False