import math
class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:

        def f(nums, r):
            ts = 0
            for i in range(len(nums)):
                ts += math.ceil(nums[i]/r)
            
            return ts


        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = (low + high)//2
            totalHours = f(nums, mid)

            if totalHours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        