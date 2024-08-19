import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        def f(nums, d):
            s = 0
            for i in range(n):
                s += math.ceil(nums[i]/d)
            return s

        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = (low + high)//2 
            total = f(nums, mid)

            if total <= threshold:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans             
        