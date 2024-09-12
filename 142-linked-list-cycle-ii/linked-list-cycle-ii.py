# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        temp = head

        while temp:
            if temp not in d:
                d[temp] = 1
            else:
                return temp
            temp = temp.next

        return
        
        return None
        