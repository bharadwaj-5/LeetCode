class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if abs(nums[left] - nums[right]) == k:
                    c += 1
        return c
