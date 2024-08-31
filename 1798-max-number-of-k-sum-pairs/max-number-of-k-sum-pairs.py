class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = 0
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]

            if total > k:
                right -= 1
            elif total < k:
                left += 1
            else:
                n += 1
                left += 1
                right -= 1 
        
        return n

        