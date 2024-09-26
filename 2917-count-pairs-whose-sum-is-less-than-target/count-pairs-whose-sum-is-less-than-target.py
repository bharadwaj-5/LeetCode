class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        for ptr1 in range(0, len(nums) - 1):
            for ptr2 in range(ptr1 + 1, len(nums)):
                if nums[ptr1] + nums[ptr2] < target:
                    pairs += 1

        return pairs
        