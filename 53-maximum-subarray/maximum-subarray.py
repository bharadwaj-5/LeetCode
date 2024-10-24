class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        s = 0
        for i in range(0, len(nums)):
            s += nums[i]
            maxi = max(s, maxi)
            if s < 0:
                s = 0
        return maxi

        