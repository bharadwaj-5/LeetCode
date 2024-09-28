class Solution:
    def findPeaks(self, nums: List[int]) -> List[int]:
        op = []

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                op.append(i)
        return op 

        