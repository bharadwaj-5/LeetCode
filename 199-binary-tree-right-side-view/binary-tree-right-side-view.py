# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = deque([root])

        while q:
            temp = deque()
            flag = False

            for i in q:
                if not flag:
                    res.append(i.val)
                    flag = True
                
                if i.right:
                    temp.append(i.right)
                if i.left:
                    temp.append(i.left)
            q = temp
        return res
        
        