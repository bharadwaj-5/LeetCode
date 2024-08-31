class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_width = 0
        zeros = 0
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            w = right - left + 1
            max_width = max(max_width, w)

        return max_width

        