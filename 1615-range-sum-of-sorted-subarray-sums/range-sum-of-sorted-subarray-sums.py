class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        o = []

        for i in range(1, len(nums)+1):
            for j in range(i):
                o.append(sum(nums[j:i]))
        
        o.sort()
        mod = 10**9 + 7
        return sum(o[left-1:right])%mod
