class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(1, n+1):
            for j in range(i):
                s += len(set(nums[j:i]))**2
        return s
        