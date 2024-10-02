# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        temp1 = None
        temp2 = None

        while(fast.next.next):
            
            fast = fast.next.next

            #Reversal through the slow pointer
            temp1 = slow.next
            slow.next = temp2
            temp2 = slow
            slow = temp1
        
        #last iteration of reversal as loop will fall short of one iteration
        head2 = slow.next
        slow.next = temp2
        head1 = slow

        maxi = -1

        while(head1.next):
            sumu = head1.val + head2.val
            if(sumu > maxi):
                maxi = sumu
            
            head1= head1.next
            head2 = head2.next
        
        sumu = head1.val + head2.val
        if(sumu > maxi):
            maxi = sumu
        return maxi