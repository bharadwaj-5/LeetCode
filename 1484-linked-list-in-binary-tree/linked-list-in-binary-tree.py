# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head and not root:
            return False
        if not head:
            return True
        if head.val != root.val:
            return False
        return self.compare(head.next, root.left) or self.compare(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return self.compare(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

        
        



