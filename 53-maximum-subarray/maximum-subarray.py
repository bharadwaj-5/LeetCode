class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxi = float('-inf')

        for i in range(0, len(nums)):
            s += nums[i]
            maxi = max(maxi, s)
            if s < 0:
                s = 0
            
        return maxi