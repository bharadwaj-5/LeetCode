# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        if not head: return None

        while head and head.val in s:
            head = head.next
        
        op = ListNode(head.val, head)

        while head and head.next:
            if head.next.val in s:
                head.next = head.next.next
            else:
                head = head.next
        
        return op.next
        