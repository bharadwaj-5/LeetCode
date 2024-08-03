class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = 0
        for n in nums:
            if p < 0:
                return False
            elif n > p:
                p = n
            p -= 1
            
        return True
        