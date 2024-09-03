# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        curr = head
        o = []
        while curr:
            o.append(curr.val)
            curr = curr.next
        print(o)
        if o == o[::-1]:
            return True
        else:
            return False

        