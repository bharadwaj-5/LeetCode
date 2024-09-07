# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = head

        k %= length

        n = length - k - 1
        new_tail = head

        for i in range(n):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head
        