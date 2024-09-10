# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return (f:=lambda n:(q:=n.next) and setattr(n,'next',ListNode(gcd(n.val,q.val),f(q))) or n)(h)
        