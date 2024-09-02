# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        n = n//2

        curr = head

        while n != 0:
            prev = curr
            curr = curr.next
            n -= 1
        
        prev.next = curr.next

        return head
