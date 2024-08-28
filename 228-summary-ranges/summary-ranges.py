class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, j = 0, 0
        n = len(nums)
        op = []
        while i < n and j < n:
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            
            if nums[i] == nums[j]:
                op.append(str(nums[i]))
            else:
                op.append(f"{nums[i]}->{nums[j]}")
            j += 1
            i = j

        return op
