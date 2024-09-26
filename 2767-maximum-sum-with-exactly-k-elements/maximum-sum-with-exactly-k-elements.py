class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = 0
        for i in range(k):
            s += nums[-1] + i
        
        return s
        