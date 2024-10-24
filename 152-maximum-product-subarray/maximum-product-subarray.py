class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1 = nums[0]
        p2 = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i]*p1, nums[i]*p2)
            p2 = min(nums[i], nums[i]*p1, nums[i]*p2)
            p1 = temp

            res = max(res, p1)
        
        return res