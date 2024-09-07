class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        max_len = 0
        zero = -1

        while right < len(nums):
            if nums[right] == 0:
                if zero != -1:
                    left = zero + 1
                zero = right
            max_len = max(max_len, right - left)
            right += 1
        
        return max_len
            
        